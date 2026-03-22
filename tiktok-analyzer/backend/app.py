"""TikTok Analyzer - Backend API"""

import json
import re
import subprocess
from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
}


def fetch_page(url):
    """Fetch a TikTok page and return the HTML."""
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.text


def extract_sigi_state(html):
    """Extract __UNIVERSAL_DATA_FOR_REHYDRATION__ or SIGI_STATE JSON from page."""
    for pattern in [
        r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>',
        r'<script id="SIGI_STATE"[^>]*>(.*?)</script>',
    ]:
        match = re.search(pattern, html, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
    return None


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/profile")
def analyze_profile():
    """Analyze a TikTok profile by username."""
    username = request.args.get("username", "").strip().lstrip("@")
    if not username:
        return jsonify({"error": "Le paramètre 'username' est requis"}), 400

    url = f"https://www.tiktok.com/@{username}"
    try:
        html = fetch_page(url)
    except requests.RequestException as e:
        return jsonify({"error": f"Impossible de charger le profil: {e}"}), 502

    data = extract_sigi_state(html)

    # Fallback: parse basic meta tags
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title")
    description = soup.find("meta", attrs={"name": "description"})
    og_image = soup.find("meta", attrs={"property": "og:image"})

    profile = {
        "username": username,
        "url": url,
        "title": title.text if title else None,
        "description": description["content"] if description else None,
        "avatar": og_image["content"] if og_image else None,
        "raw_data_available": data is not None,
    }

    if data:
        # Try to extract stats from universal data
        try:
            default_scope = data.get("__DEFAULT_SCOPE__", {})
            user_detail = default_scope.get("webapp.user-detail", {})
            user_info = user_detail.get("userInfo", {})
            stats = user_info.get("stats", {})
            user = user_info.get("user", {})

            profile.update({
                "nickname": user.get("nickname"),
                "bio": user.get("signature"),
                "verified": user.get("verified", False),
                "followers": stats.get("followerCount", 0),
                "following": stats.get("followingCount", 0),
                "likes": stats.get("heartCount", 0),
                "videos": stats.get("videoCount", 0),
            })
        except (KeyError, TypeError):
            pass

    return jsonify(profile)


@app.route("/api/video")
def analyze_video():
    """Analyze a TikTok video by URL using yt-dlp."""
    video_url = request.args.get("url", "").strip()
    if not video_url:
        return jsonify({"error": "Le paramètre 'url' est requis"}), 400

    if "tiktok.com" not in video_url:
        return jsonify({"error": "URL TikTok invalide"}), 400

    try:
        result = subprocess.run(
            ["yt-dlp", "--dump-json", "--no-download", video_url],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return jsonify({"error": "Impossible d'analyser la vidéo", "details": result.stderr}), 502

        info = json.loads(result.stdout)

        video = {
            "title": info.get("title"),
            "description": info.get("description"),
            "creator": info.get("creator") or info.get("uploader"),
            "uploader_id": info.get("uploader_id"),
            "duration": info.get("duration"),
            "views": info.get("view_count"),
            "likes": info.get("like_count"),
            "comments": info.get("comment_count"),
            "shares": info.get("repost_count"),
            "upload_date": info.get("upload_date"),
            "thumbnail": info.get("thumbnail"),
            "tags": info.get("tags", []),
            "music": {
                "title": info.get("track"),
                "artist": info.get("artist"),
            },
            "resolution": f"{info.get('width', '?')}x{info.get('height', '?')}",
        }
        return jsonify(video)

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Timeout lors de l'analyse"}), 504
    except (json.JSONDecodeError, OSError) as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/hashtag")
def analyze_hashtag():
    """Get info about a TikTok hashtag/challenge."""
    tag = request.args.get("tag", "").strip().lstrip("#")
    if not tag:
        return jsonify({"error": "Le paramètre 'tag' est requis"}), 400

    url = f"https://www.tiktok.com/tag/{tag}"
    try:
        html = fetch_page(url)
    except requests.RequestException as e:
        return jsonify({"error": f"Impossible de charger le hashtag: {e}"}), 502

    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title")
    description = soup.find("meta", attrs={"name": "description"})

    data = extract_sigi_state(html)

    result = {
        "hashtag": f"#{tag}",
        "url": url,
        "title": title.text if title else None,
        "description": description["content"] if description else None,
        "raw_data_available": data is not None,
    }

    if data:
        try:
            default_scope = data.get("__DEFAULT_SCOPE__", {})
            challenge_detail = default_scope.get("webapp.challenge-detail", {})
            challenge_info = challenge_detail.get("challengeInfo", {})
            stats = challenge_info.get("stats", {})

            result.update({
                "views": stats.get("viewCount", 0),
                "video_count": stats.get("videoCount", 0),
            })
        except (KeyError, TypeError):
            pass

    return jsonify(result)


if __name__ == "__main__":
    print("🚀 TikTok Analyzer API démarré sur http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
