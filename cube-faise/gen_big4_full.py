import sys
sys.path.insert(0, '.')
exec(open('gen_pptx_part1.py').read())

prs = mk()
print('Generating Big4 PPTX...')

# S1 COVER
s = sl(prs)
rc(s, Inches(0), Inches(0), Inches(5), H, NAVY)
rc(s, Inches(5), Inches(0), Inches(8.333), H, WHITE)
tx(s, 'CUBE', Inches(1.5), Inches(2.5), Inches(3), Inches(1), 54, True, GOLD, PP_ALIGN.CENTER)
tx(s, 'x  FAISE', Inches(1.5), Inches(3.4), Inches(3), Inches(0.6), 28, False, WHITE, PP_ALIGN.CENTER)
tx(s, 'CONFIDENTIEL', Inches(1.5), Inches(6.5), Inches(3), Inches(0.3), 8, False, MGRAY, PP_ALIGN.CENTER)
mtx(s, [
    ('CUBE x FAISE', 36, True, NAVY),
    ('', 4, False, None),
    ('Transformer l\'epargne de la diaspora', 16, False, GOLD),
    ('en moteur de croissance des PME senegalaises', 16, False, GOLD),
    ('', 4, False, None),
    ('Proposition de partenariat strategique', 14, False, MGRAY),
    ('', 4, False, None),
    ('Cabinet Carree  |  ccarree.com  |  Avril 2026', 11, False, MGRAY),
], Inches(5.8), Inches(2), Inches(6.5), Inches(4), PP_ALIGN.LEFT)
print('  Slide 1: Cover')

# S2 SOMMAIRE
s = sl(prs)
hdr(s, 'SOMMAIRE', '')
tx(s, 'Sommaire', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 28, True, NAVY)
items = [
    '01.  Cabinet Carree — Qui sommes-nous',
    '02.  Le Constat — Un potentiel bloque',
    '03.  Cas Concrets PME',
    '04.  La Solution CUBE',
    '05.  Le Flux CUBE en 6 etapes',
    '06.  Convergence FAISE x CUBE',
    '07.  Voies de Partenariat',
    '08.  Modele economique partage',
    '09.  Resultats Attendus',
    '10.  Next Steps',
]
lines = []
for it in items:
    num = it[:3]
    rest = it[3:]
    lines.append((it, 16, False, NAVY))
    lines.append(('', 4, False, None))
mtx(s, lines, Inches(1.5), Inches(1.8), Inches(10), Inches(5), PP_ALIGN.LEFT)
print('  Slide 2: Sommaire')

# S3 CABINET CARREE
s = sl(prs)
hdr(s, 'QUI SOMMES-NOUS', '01')
tx(s, 'Un cabinet ancre dans la realite des PME africaines', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
# 3 stat boxes
for i, (num, lab) in enumerate([('70 000+', 'clients accompagnes'), ('50+', 'pays'), ('7 ans', "d'experience")]):
    x = Inches(0.7 + i * 4)
    rc(s, x, Inches(1.8), Inches(3.5), Inches(1.4), LGRAY, GOLD)
    tx(s, num, x, Inches(1.9), Inches(3.5), Inches(0.7), 32, True, GOLD, PP_ALIGN.CENTER)
    tx(s, lab, x, Inches(2.6), Inches(3.5), Inches(0.4), 11, False, MGRAY, PP_ALIGN.CENTER)
mtx(s, [
    ('Fonde en janvier 2019 a Dakar, Senegal', 12, True, DTXT),
    ('Conseil strategique, accompagnement TPE/PME, gestion de projets, transformation digitale', 11, False, MGRAY),
    ('', 4, False, None),
    ('Programme SENEV : accelerateur international pour PME africaines', 11, False, MGRAY),
    ('Cas reel : BMR (Body Medical Repair) — subvention de 20M FCFA obtenue en 9 mois', 11, True, NAVY),
    ('', 4, False, None),
    ('Clients : PME, multinationales, ONG, institutions publiques', 11, False, MGRAY),
    ('Site : ccarree.com', 11, False, GOLD),
], Inches(0.7), Inches(3.5), Inches(11.5), Inches(3.5))
print('  Slide 3: Cabinet Carree')

# S4 LE CONSTAT
s = sl(prs)
hdr(s, 'LE CONSTAT', '02')
tx(s, 'Un potentiel immense, bloque par un deficit de financement', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
cards = [
    ('PME SENEGALAISES', 'Rentables mais incapables de financer stock au bon moment. Taux bancaires: 12-18%. Garanties inaccessibles.', RED, '90% du tissu economique'),
    ('DIASPORA', '+200 Mds FCFA/an transferes. 90% va a la consommation. Aucun vehicule d\'investissement structure.', BLUE, '+200 Mds FCFA/an'),
    ('BANQUES CLASSIQUES', 'Asymetrie info, garanties insuffisantes, processus de 3-6 mois. PME sous-bancarisees.', ORANGE, '12-18% taux'),
    ('FAISE ACTUEL', '5-15M FCFA/projet. 643 projets en 15 ans. "Ne peut satisfaire toutes les demandes."', GREEN, '643 projets / 15 ans'),
]
for i, (title, desc, color, stat) in enumerate(cards):
    col = i % 2
    row = i // 2
    x = Inches(0.7 + col * 6.2)
    y = Inches(1.7 + row * 2.7)
    rc(s, x, y, Inches(5.8), Inches(2.4), LGRAY)
    rc(s, x, y, Inches(0.06), Inches(2.4), color)
    tx(s, title, Inches(0.3) + x, y + Inches(0.2), Inches(5.2), Inches(0.3), 13, True, NAVY)
    tx(s, desc, Inches(0.3) + x, y + Inches(0.6), Inches(5.2), Inches(1), 10, False, MGRAY)
    tx(s, stat, Inches(0.3) + x, y + Inches(1.7), Inches(5.2), Inches(0.5), 18, True, GOLD)
print('  Slide 4: Le Constat')

# S5 CAS CONCRETS
s = sl(prs)
hdr(s, 'SUR LE TERRAIN', '03')
tx(s, 'Trois PME accompagnees — le probleme en chiffres', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
cases = [
    ('Stamipol Group', 'Cosmetique & Bien-etre', 'Maristes, Dakar | 11-50 employes', 'Stock importe: 25M FCFA | Cycle: 6 mois', 'Marge: 100-150%', 'Refus bancaire faute de track record international', '25M'),
    ("Fasha'Style", 'Mode & Textile', 'Ouest Foire, Dakar | fashastyle.com', 'Stock saisonnier: 12M FCFA | Rotation 3x/an', 'Marge: 80-120%', 'Impossible de financer 2 saisons simultanement', '12M'),
    ('PME Distribution', 'Alimentaire, Dakar', 'CA annuel: 85M FCFA', 'Stock necessaire: 20M/trimestre', 'Marge: 35-45%', 'Stock limite a 8M = 40% du CA perdu', '20M'),
]
for i, (name, sector, loc, stock, marge, problem, kpi) in enumerate(cases):
    y = Inches(1.7 + i * 1.8)
    rc(s, Inches(0.7), y, Inches(11.9), Inches(1.6), LGRAY)
    rc(s, Inches(0.7), y, Inches(0.06), Inches(1.6), GOLD)
    tx(s, kpi, Inches(0.9), y + Inches(0.15), Inches(1.2), Inches(0.6), 22, True, GOLD)
    tx(s, 'FCFA', Inches(0.9), y + Inches(0.75), Inches(1.2), Inches(0.3), 8, False, MGRAY)
    tx(s, name, Inches(2.3), y + Inches(0.15), Inches(3), Inches(0.3), 14, True, NAVY)
    tx(s, sector + ' | ' + loc, Inches(2.3), y + Inches(0.5), Inches(4), Inches(0.3), 9, False, MGRAY)
    tx(s, stock + ' | ' + marge, Inches(2.3), y + Inches(0.8), Inches(5), Inches(0.3), 10, False, DTXT)
    tx(s, 'Probleme: ' + problem, Inches(2.3), y + Inches(1.1), Inches(9), Inches(0.3), 10, True, RED)
print('  Slide 5: Cas Concrets')

# S6 SOLUTION CUBE
s = sl(prs)
hdr(s, 'LA REPONSE', '04')
tx(s, 'CUBE — Connecter l\'epargne diaspora aux actifs PME', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
mtx(s, [
    ('Plateforme web de crowdfunding d\'actifs : la diaspora investit directement dans les stocks de PME pre-qualifiees par Cabinet Carree.', 13, False, DTXT),
    ('', 4, False, None),
    ('Le mecanisme:', 14, True, NAVY),
    ('1. Cabinet Carree acquiert le stock pour le compte de l\'investisseur', 12, False, DTXT),
    ('2. Le stock est mis a disposition de la PME', 12, False, DTXT),
    ('3. La PME revend avec ses marges habituelles (35% a 200%)', 12, False, DTXT),
    ('4. L\'investisseur recupere capital + rendement garanti', 12, False, DTXT),
    ('', 4, False, None),
    ('Garantie triple: stock physique + PME pre-qualifiees + partenaire bancaire (Cofina/SGBS/Microcash)', 12, True, NAVY),
], Inches(0.7), Inches(1.7), Inches(7), Inches(4))
# 3 formula cards
for i, (name, rate, dur, desc) in enumerate([
    ('CUBE Starter', '50%', '6 mois', 'Court terme, rotation rapide'),
    ('CUBE Premium', '100%', '12 mois', 'Formule phare, haute marge'),
    ('CUBE Elite', '150%', '18 mois', 'Long terme, diversifie'),
]):
    x = Inches(8.2 + i * 0) if i == 0 else Inches(8.2)
    y = Inches(1.7 + i * 1.8)
    border = GOLD if i == 1 else LGRAY
    rc(s, x, y, Inches(4.5), Inches(1.5), LGRAY, border)
    tx(s, name, x + Inches(0.2), y + Inches(0.1), Inches(4), Inches(0.3), 12, True, NAVY)
    tx(s, rate, x + Inches(0.2), y + Inches(0.4), Inches(2), Inches(0.6), 28, True, GOLD)
    tx(s, '/ ' + dur, x + Inches(1.8), y + Inches(0.55), Inches(2), Inches(0.3), 11, False, MGRAY)
    tx(s, desc, x + Inches(0.2), y + Inches(1), Inches(4), Inches(0.3), 9, False, MGRAY)
print('  Slide 6: Solution CUBE')

# S7 FLUX 6 ETAPES
s = sl(prs)
hdr(s, 'LE MECANISME', '05')
tx(s, 'Le flux CUBE en 6 etapes — simple, transparent, securise', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
steps = [
    ('1', 'Investisseur', 'Inscription sur CUBE,\nconsulte opportunites'),
    ('2', 'Investissement', 'Choisit un lot,\ninvestit via virement'),
    ('3', 'Securisation', 'Fonds securises\nchez partenaire bancaire'),
    ('4', 'Acquisition', 'Cabinet acquiert stock\npour la PME'),
    ('5', 'Vente PME', 'PME revend stock\navec ses marges'),
    ('6', 'Redistribution', 'Capital + rendement\nretourne investisseur'),
]
for i, (num, title, desc) in enumerate(steps):
    x = Inches(0.5 + i * 2.1)
    y = Inches(2)
    rc(s, x, y, Inches(1.9), Inches(3.5), LGRAY, NAVY)
    rc(s, x + Inches(0.7), y + Inches(0.2), Inches(0.5), Inches(0.5), GOLD)
    tx(s, num, x + Inches(0.7), y + Inches(0.2), Inches(0.5), Inches(0.5), 14, True, NAVY, PP_ALIGN.CENTER)
    tx(s, title, x + Inches(0.1), y + Inches(0.9), Inches(1.7), Inches(0.4), 11, True, NAVY, PP_ALIGN.CENTER)
    tx(s, desc, x + Inches(0.1), y + Inches(1.4), Inches(1.7), Inches(1.5), 9, False, MGRAY, PP_ALIGN.CENTER)
    if i < 5:
        tx(s, '>', Inches(0.5 + (i+1) * 2.1 - 0.25), y + Inches(1.5), Inches(0.3), Inches(0.3), 20, True, GOLD, PP_ALIGN.CENTER)
print('  Slide 7: Flux 6 etapes')

# S8 CONVERGENCE FAISE x CUBE
s = sl(prs)
hdr(s, 'SYNERGIE', '06')
tx(s, 'Pourquoi FAISE et CUBE sont des partenaires naturels', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
tbl = s.shapes.add_table(6, 4, Inches(0.7), Inches(1.7), Inches(11.9), Inches(3.5)).table
tbl.columns[0].width = Inches(3)
tbl.columns[1].width = Inches(3)
tbl.columns[2].width = Inches(3)
tbl.columns[3].width = Inches(2.9)
hdrs = ['', 'FAISE seul', 'CUBE seul', 'FAISE x CUBE']
rows_data = [
    ['Financement max/projet', '5-15M FCFA', 'Illimite (crowd)', 'DECUPLE'],
    ['Beneficiaires/an', '~43 projets', '100+ PME', '500+ PME'],
    ['Retour sur fonds', 'Non (subvention)', '50-150%', 'Fonds revolving'],
    ['Tracabilite', 'Manuelle', 'Digitale temps reel', 'Digitale + institutionnelle'],
    ['Impact diaspora', 'Indirect', 'Direct', 'Direct + labellise Etat'],
]
for j, h in enumerate(hdrs):
    cell = tbl.cell(0, j)
    cell.text = h
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY
    for p in cell.text_frame.paragraphs:
        for r in p.runs:
            r.font.color.rgb = WHITE
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.name = 'Calibri'
for i, row in enumerate(rows_data):
    for j, val in enumerate(row):
        cell = tbl.cell(i+1, j)
        cell.text = val
        if j == 3:
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(255, 248, 225)
        for p in cell.text_frame.paragraphs:
            for r in p.runs:
                r.font.size = Pt(10)
                r.font.name = 'Calibri'
                r.font.bold = (j == 3)
                if j == 3: r.font.color.rgb = NAVY
tx(s, '"Le FAISE reconnait ne pouvoir satisfaire toutes les demandes eligibles." — CUBE est la reponse.', Inches(0.7), Inches(5.5), Inches(11.9), Inches(0.5), 12, True, GOLD, PP_ALIGN.CENTER)
print('  Slide 8: Convergence')

# S9 PARTENARIAT
s = sl(prs)
hdr(s, 'PROPOSITION', '07')
tx(s, 'Trois modalites de partenariat — selon vos priorites', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
opts = [
    ('OPTION A — RECOMMANDEE', 'MARQUE BLANCHE', '"CUBE, propulse par FAISE"', 'FAISE apporte: visibilite, legitimite, reseau diaspora\nCabinet Carree: technologie, expertise PME, operations\nAvantage: produit a votre nom, sans dev tech', GOLD),
    ('OPTION B', 'CO-BRANDING', '"FAISE x CUBE | Cabinet Carree"', 'Partenariat egal, communication conjointe\nGouvernance partagee\nIdeal pour phase pilote', NAVY),
    ('OPTION C', 'FONDS DELEGUE', 'FAISE delegue 500M FCFA', 'Cabinet deploie via CUBE, rendements revolving\nFAISE multiplie son impact\nSans gerer l\'operationnel', NAVY),
]
for i, (label, title, sub, desc, border) in enumerate(opts):
    x = Inches(0.7 + i * 4.1)
    rc(s, x, Inches(1.7), Inches(3.8), Inches(5), LGRAY, border)
    rc(s, x, Inches(1.7), Inches(3.8), Inches(0.06), border)
    tx(s, label, x + Inches(0.2), Inches(1.85), Inches(3.4), Inches(0.3), 8, True, border)
    tx(s, title, x + Inches(0.2), Inches(2.2), Inches(3.4), Inches(0.4), 18, True, NAVY)
    tx(s, sub, x + Inches(0.2), Inches(2.7), Inches(3.4), Inches(0.4), 11, True, GOLD)
    tx(s, desc, x + Inches(0.2), Inches(3.3), Inches(3.4), Inches(3), 10, False, MGRAY)
print('  Slide 9: Partenariat')

# S10 MODELE ECONOMIQUE
s = sl(prs)
sbg(s, NAVY)
hdr_nums = [
    ('500M FCFA', 'Fonds FAISE delegues'),
    ('50 lots', 'x 10M FCFA / PME'),
    ('80%', 'Rendement moyen / 12 mois'),
    ('900M', 'Retour brut'),
    ('820M', 'Retour net FAISE (+64%)'),
    ('3 000M+', 'Finances cumules en 3 ans'),
]
rc(s, Inches(0), Inches(0), W, Inches(0.6), GOLD)
tx(s, 'LES CHIFFRES', Inches(0.5), Inches(0.12), Inches(5), Inches(0.4), 9, True, NAVY)
tx(s, '08', Inches(12), Inches(0.12), Inches(1), Inches(0.4), 9, False, NAVY, PP_ALIGN.RIGHT)
tx(s, '500M FCFA  >  3 000M+ en 3 ans', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 28, True, WHITE)
for i, (num, label) in enumerate(hdr_nums):
    col = i % 3
    row = i // 3
    x = Inches(0.7 + col * 4.2)
    y = Inches(1.8 + row * 2.8)
    rc(s, x, y, Inches(3.8), Inches(2.4), RGBColor(0, 55, 100))
    tx(s, num, x + Inches(0.3), y + Inches(0.3), Inches(3.2), Inches(0.8), 34, True, GOLD, PP_ALIGN.CENTER)
    tx(s, label, x + Inches(0.3), y + Inches(1.3), Inches(3.2), Inches(0.5), 12, False, WHITE, PP_ALIGN.CENTER)
    if i < 5:
        arrow_x = x + Inches(3.9) if col < 2 else Inches(0.3)
        if col < 2:
            tx(s, '>', x + Inches(3.85), y + Inches(0.8), Inches(0.3), Inches(0.3), 18, True, GOLD)
rc(s, Inches(0), Inches(7.2), W, Inches(0.3), GOLD)
tx(s, 'CONFIDENTIEL  |  Cabinet Carree x CUBE', Inches(0.5), Inches(7.22), Inches(12), Inches(0.25), 7, False, NAVY)
print('  Slide 10: Modele economique')

# S11 RESULTATS ATTENDUS
s = sl(prs)
hdr(s, 'IMPACT A 3 ANS', '09')
tx(s, 'Diaspora, PME, tissu industriel — un impact mesurable', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
impacts = [
    ('DIASPORA', BLUE, ['500+ investisseurs actifs', '2 Mds FCFA mobilises', 'Rendements 50-150%', 'Tracabilite digitale', "Sentiment d'impact"]),
    ('PME', GREEN, ['100+ PME financees/an', '+40% CA moyen', 'Stock optimise', 'Formalisation comptable', 'Preparation bancarisation']),
    ('TISSU INDUSTRIEL', GOLD, ['3 secteurs pilotes', 'Expansion UEMOA', "Cote d'Ivoire, Mali", 'Creation emplois', 'Contribution PSE']),
]
for i, (title, color, items) in enumerate(impacts):
    x = Inches(0.7 + i * 4.2)
    rc(s, x, Inches(1.7), Inches(3.8), Inches(5), LGRAY)
    rc(s, x, Inches(1.7), Inches(3.8), Inches(0.06), color)
    tx(s, title, x + Inches(0.3), Inches(1.9), Inches(3.2), Inches(0.4), 14, True, NAVY)
    lines = []
    for it in items:
        lines.append(('> ' + it, 11, False, DTXT))
        lines.append(('', 4, False, None))
    mtx(s, lines, x + Inches(0.3), Inches(2.5), Inches(3.2), Inches(4))
print('  Slide 11: Resultats')

# S12 NEXT STEPS
s = sl(prs)
hdr(s, 'CALENDRIER', '10')
tx(s, 'Prochaines etapes — demarrons ensemble', Inches(0.7), Inches(0.9), Inches(11), Inches(0.6), 24, True, NAVY)
timeline = [
    ('Avr 2026', 'Protocole d\'accord FAISE x Cabinet Carree'),
    ('Mai 2026', 'Validation cadre juridique + partenaire bancaire'),
    ('Juin 2026', 'Pilote: 5 PME, 50 investisseurs, 50M FCFA'),
    ('Sept 2026', 'Bilan pilote + ajustements'),
    ('Dec 2026', 'Lancement officiel — Journee nationale Diaspora'),
    ('2027', 'Deploiement plein regime + expansion UEMOA'),
]
for i, (date, desc) in enumerate(timeline):
    y = Inches(1.8 + i * 0.85)
    rc(s, Inches(0.7), y, Inches(0.15), Inches(0.15), GOLD)
    tx(s, date, Inches(1.1), y - Inches(0.05), Inches(2), Inches(0.3), 13, True, GOLD)
    tx(s, desc, Inches(3.5), y - Inches(0.05), Inches(9), Inches(0.3), 13, False, DTXT)

mtx(s, [
    ('', 8, False, None),
    ('Cabinet Carree', 14, True, NAVY),
    ('ccarree.com', 12, False, GOLD),
    ('Dakar, VDN lot 67 Bande Verte, Immeuble Bilguiss 4eme etage', 10, False, MGRAY),
], Inches(0.7), Inches(6), Inches(11), Inches(1.2))
print('  Slide 12: Next Steps')

out = '/home/user/bookish-octo-engine/cube-faise/CUBE_FAISE_Big4.pptx'
prs.save(out)
import os
sz = os.path.getsize(out)
print(f'\nBig4 PPTX saved: {out} ({sz/1024:.1f} KB)')
