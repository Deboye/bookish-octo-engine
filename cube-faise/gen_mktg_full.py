exec(open('gen_pptx_part1.py').read())

prs = mk()
print('Generating Marketing PPTX...')

def mhdr(s, label, num):
    sbg(s, DGREEN)
    rc(s, Inches(0.8), Inches(7.15), Inches(11.7), Inches(0.02), GOLD)
    tx(s, label, Inches(0.8), Inches(0.35), Inches(5), Inches(0.3), 10, True, BGREEN)
    tx(s, num, Inches(11.5), Inches(0.15), Inches(1.5), Inches(0.6), 48, True, RGBColor(30,70,38), PP_ALIGN.RIGHT)
    tx(s, 'CUBE x FAISE  |  Cabinet Carree  |  CONFIDENTIEL', Inches(0.8), Inches(7.22), Inches(11), Inches(0.2), 7, False, MUTED)

# S1 COVER
s = sl(prs)
sbg(s, DGREEN)
rc(s, Inches(8), Inches(0.8), Inches(4.5), Inches(4.5), DGREEN, GOLD)
rc(s, Inches(8.5), Inches(1.3), Inches(3.5), Inches(3.5), DGREEN, BGREEN)
tx(s, 'CUBE', Inches(0.8), Inches(1.5), Inches(6), Inches(1), 60, True, GOLD)
tx(s, 'x  FAISE', Inches(0.8), Inches(2.5), Inches(6), Inches(0.7), 36, True, WHITE)
mtx(s, [
    ('', 8, False, None),
    ("Transformer l'epargne de la diaspora", 18, False, GOLD),
    ('en moteur de croissance des PME senegalaises', 18, False, GOLD),
    ('', 8, False, None),
    ('Proposition de partenariat strategique', 13, False, MUTED),
], Inches(0.8), Inches(3.5), Inches(7), Inches(2.5))
tx(s, 'Cabinet Carree  |  ccarree.com  |  Avril 2026', Inches(0.8), Inches(6.5), Inches(6), Inches(0.3), 11, False, MUTED)
rc(s, Inches(0.8), Inches(7.15), Inches(11.7), Inches(0.02), GOLD)
print('  Slide 1: Cover')

# S2 SOMMAIRE
s = sl(prs)
mhdr(s, 'SOMMAIRE', '')
tx(s, 'Sommaire', Inches(0.8), Inches(0.9), Inches(11), Inches(0.6), 32, True, WHITE)
items = ['01  Cabinet Carree', '02  Le Constat', '03  Cas Concrets PME', '04  La Solution CUBE',
         '05  Flux CUBE 6 etapes', '06  Convergence FAISE x CUBE', '07  Voies de Partenariat',
         '08  Modele economique', '09  Resultats Attendus', '10  Next Steps']
lines = []
for it in items:
    lines.append((it[:2], 16, True, GOLD))
for i, it in enumerate(items):
    lines[i] = (it, 15, False, WHITE)
lines2 = []
for it in items:
    lines2.append((it, 15, False, WHITE))
    lines2.append(('', 6, False, None))
mtx(s, lines2, Inches(1.5), Inches(1.8), Inches(10), Inches(5.2))
print('  Slide 2: Sommaire')

# S3 CABINET CARREE
s = sl(prs)
mhdr(s, 'QUI SOMMES-NOUS', '01')
tx(s, 'Un cabinet ancre dans la realite des PME africaines', Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 26, True, WHITE)
for i, (num, lab) in enumerate([('70 000+', 'clients'), ('50+', 'pays'), ('7 ans', "d'experience")]):
    x = Inches(0.8 + i * 4.1)
    rc(s, x, Inches(1.7), Inches(3.7), Inches(1.5), CDBG)
    tx(s, num, x, Inches(1.8), Inches(3.7), Inches(0.8), 36, True, GOLD, PP_ALIGN.CENTER)
    tx(s, lab, x, Inches(2.6), Inches(3.7), Inches(0.3), 11, False, MUTED, PP_ALIGN.CENTER)
mtx(s, [
    ('Fonde en janvier 2019 a Dakar, Senegal', 12, True, WHITE),
    ('Conseil strategique, accompagnement TPE/PME, transformation digitale', 11, False, MUTED),
    ('', 4, False, None),
    ('Programme SENEV : accelerateur international pour PME africaines', 11, False, MUTED),
    ('Cas reel : BMR — subvention de 20M FCFA obtenue en 9 mois', 11, True, GOLD),
    ('', 4, False, None),
    ('ccarree.com', 11, False, AGREEN),
], Inches(0.8), Inches(3.5), Inches(11.5), Inches(3.5))
print('  Slide 3: Cabinet Carree')

# S4 LE CONSTAT
s = sl(prs)
mhdr(s, 'LE PROBLEME', '02')
tx(s, 'Un potentiel immense, bloque', Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 26, True, WHITE)
cards = [
    ('PME', 'Rentables mais stock non finance. Taux 12-18%.', RED, '90%', 'du tissu economique'),
    ('DIASPORA', '90% des transferts = consommation. 0 vehicule investissement.', BLUE, '+200Mds', 'FCFA/an transferes'),
    ('BANQUES', 'Asymetrie info, garanties excessives, processus 3-6 mois.', ORANGE, '12-18%', 'taux bancaires'),
    ('FAISE', '5-15M/projet. 643 projets en 15 ans. Insuffisant.', GOLD, '643', 'projets / 15 ans'),
]
for i, (title, desc, color, kpi, kpi_lab) in enumerate(cards):
    col = i % 2
    row = i // 2
    x = Inches(0.8 + col * 6.2)
    y = Inches(1.7 + row * 2.7)
    rc(s, x, y, Inches(5.8), Inches(2.4), CDBG)
    rc(s, x, y, Inches(0.06), Inches(2.4), color)
    tx(s, title, x + Inches(0.3), y + Inches(0.15), Inches(3), Inches(0.3), 13, True, WHITE)
    tx(s, desc, x + Inches(0.3), y + Inches(0.55), Inches(5), Inches(0.8), 10, False, MUTED)
    tx(s, kpi, x + Inches(0.3), y + Inches(1.5), Inches(3), Inches(0.6), 24, True, GOLD)
    tx(s, kpi_lab, x + Inches(2.5), y + Inches(1.65), Inches(3), Inches(0.3), 9, False, MUTED)
print('  Slide 4: Le Constat')

# S5 CAS CONCRETS
s = sl(prs)
mhdr(s, 'SUR LE TERRAIN', '03')
tx(s, 'Trois PME — le probleme en chiffres', Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 26, True, WHITE)
cases = [
    ('Stamipol Group', 'Cosmetique', '25M FCFA', 'Marge 100-150%', 'Refus bancaire'),
    ("Fasha'Style", 'Mode & Textile', '12M FCFA', 'Marge 80-120%', '2 saisons impossibles'),
    ('PME Distribution', 'Alimentaire', '20M FCFA', 'Marge 35-45%', '40% CA perdu'),
]
for i, (name, sector, stock, marge, pb) in enumerate(cases):
    x = Inches(0.8 + i * 4.2)
    rc(s, x, Inches(1.7), Inches(3.8), Inches(4.8), CDBG)
    tx(s, name, x + Inches(0.3), Inches(1.85), Inches(3.2), Inches(0.4), 16, True, WHITE)
    tx(s, sector, x + Inches(0.3), Inches(2.3), Inches(3.2), Inches(0.3), 10, False, AGREEN)
    tx(s, stock, x + Inches(0.3), Inches(2.9), Inches(3.2), Inches(0.7), 30, True, GOLD, PP_ALIGN.CENTER)
    tx(s, 'stock necessaire', x + Inches(0.3), Inches(3.55), Inches(3.2), Inches(0.3), 9, False, MUTED, PP_ALIGN.CENTER)
    tx(s, marge, x + Inches(0.3), Inches(4.1), Inches(3.2), Inches(0.3), 13, True, AGREEN)
    rc(s, x + Inches(0.3), Inches(4.7), Inches(3.2), Inches(0.02), RED)
    tx(s, pb, x + Inches(0.3), Inches(4.9), Inches(3.2), Inches(0.5), 10, True, RGBColor(255,130,130))
print('  Slide 5: Cas Concrets')

# S6 SOLUTION
s = sl(prs)
mhdr(s, 'LA REPONSE', '04')
tx(s, "CUBE — L'epargne diaspora finance les PME", Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 26, True, WHITE)
mtx(s, [
    ('Plateforme web de crowdfunding d\'actifs', 14, True, GOLD),
    ('La diaspora investit directement dans les stocks de PME pre-qualifiees.', 12, False, MUTED),
    ('', 6, False, None),
    ('Cabinet acquiert le stock > PME revend > Investisseur recupere capital + rendement', 12, False, WHITE),
    ('', 6, False, None),
    ('Garantie triple: stock physique + PME pre-qualifiees + partenaire bancaire', 11, True, AGREEN),
], Inches(0.8), Inches(1.7), Inches(7), Inches(2.5))
for i, (name, rate, dur, desc) in enumerate([
    ('Starter', '50%', '6 mois', 'Court terme'),
    ('Premium', '100%', '12 mois', 'Formule phare'),
    ('Elite', '150%', '18 mois', 'Long terme'),
]):
    x = Inches(0.8 + i * 4.2)
    border = GOLD if i == 1 else CDBG
    rc(s, x, Inches(4.5), Inches(3.8), Inches(2.2), CDBG, border)
    tx(s, 'CUBE ' + name, x + Inches(0.3), Inches(4.6), Inches(3.2), Inches(0.3), 12, True, WHITE)
    tx(s, rate, x + Inches(0.3), Inches(4.9), Inches(2), Inches(0.7), 32, True, GOLD)
    tx(s, '/ ' + dur, x + Inches(2.2), Inches(5.1), Inches(1.3), Inches(0.3), 11, False, MUTED)
    tx(s, desc, x + Inches(0.3), Inches(5.7), Inches(3.2), Inches(0.3), 9, False, MUTED)
print('  Slide 6: Solution')

# S7 FLUX
s = sl(prs)
mhdr(s, 'LE MECANISME', '05')
tx(s, 'Simple, transparent, securise', Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 26, True, WHITE)
steps = [
    ('1', 'Investisseur', 'Inscription CUBE'),
    ('2', 'Investissement', 'Virement/mobile money'),
    ('3', 'Securisation', 'Fonds en banque'),
    ('4', 'Acquisition', 'Cabinet achete stock'),
    ('5', 'Vente', 'PME revend'),
    ('6', 'Redistribution', 'Capital + rendement'),
]
for i, (num, title, desc) in enumerate(steps):
    x = Inches(0.5 + i * 2.1)
    rc(s, x, Inches(2.2), Inches(1.9), Inches(3), CDBG, MGREEN)
    rc(s, x + Inches(0.7), Inches(2.35), Inches(0.5), Inches(0.5), GOLD)
    tx(s, num, x + Inches(0.7), Inches(2.35), Inches(0.5), Inches(0.5), 14, True, DGREEN, PP_ALIGN.CENTER)
    tx(s, title, x + Inches(0.1), Inches(3.1), Inches(1.7), Inches(0.4), 12, True, WHITE, PP_ALIGN.CENTER)
    tx(s, desc, x + Inches(0.1), Inches(3.6), Inches(1.7), Inches(1), 9, False, MUTED, PP_ALIGN.CENTER)
    if i < 5:
        tx(s, '>', Inches(0.5 + (i+1) * 2.1 - 0.25), Inches(3.3), Inches(0.3), Inches(0.3), 18, True, GOLD, PP_ALIGN.CENTER)
print('  Slide 7: Flux')

# S8 CONVERGENCE
s = sl(prs)
mhdr(s, 'SYNERGIE', '06')
tx(s, 'FAISE + CUBE = Impact demultiplie', Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 26, True, WHITE)
cols = [('FAISE seul', MGREEN), ('CUBE seul', BGREEN), ('FAISE x CUBE', GOLD)]
metrics = [
    ('Financement', '5-15M FCFA', 'Illimite', 'DECUPLE'),
    ('Beneficiaires/an', '~43', '100+', '500+'),
    ('Retour fonds', 'Subvention', '50-150%', 'Revolving'),
    ('Tracabilite', 'Manuelle', 'Digitale', 'Digitale + Etat'),
]
for j, (col_name, col_color) in enumerate(cols):
    x = Inches(3.8 + j * 3.2)
    rc(s, x, Inches(1.6), Inches(3), Inches(0.5), col_color)
    tx(s, col_name, x, Inches(1.62), Inches(3), Inches(0.45), 10, True, WHITE if j < 2 else DGREEN, PP_ALIGN.CENTER)
for i, (metric, v1, v2, v3) in enumerate(metrics):
    y = Inches(2.3 + i * 1.1)
    tx(s, metric, Inches(0.8), y, Inches(2.8), Inches(0.4), 11, True, WHITE)
    for j, v in enumerate([v1, v2, v3]):
        x = Inches(3.8 + j * 3.2)
        rc(s, x, y, Inches(3), Inches(0.8), CDBG)
        clr = GOLD if j == 2 else MUTED
        tx(s, v, x, y + Inches(0.15), Inches(3), Inches(0.5), 13, j==2, clr, PP_ALIGN.CENTER)
tx(s, '"Le FAISE ne peut satisfaire toutes les demandes. CUBE est la reponse."', Inches(0.8), Inches(6.3), Inches(11.5), Inches(0.5), 12, True, GOLD, PP_ALIGN.CENTER)
print('  Slide 8: Convergence')

# S9 PARTENARIAT
s = sl(prs)
mhdr(s, 'PROPOSITION', '07')
tx(s, 'Trois modalites — selon vos priorites', Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 26, True, WHITE)
opts = [
    ('A  RECOMMANDEE', 'MARQUE BLANCHE', '"CUBE propulse par FAISE"', 'FAISE: visibilite, reseau\nCC: tech, expertise, ops', GOLD),
    ('B', 'CO-BRANDING', '"FAISE x CUBE"', 'Communication conjointe\nGouvernance partagee', BGREEN),
    ('C', 'FONDS DELEGUE', '500M FCFA revolving', 'CC deploie via CUBE\nRendements reversees FAISE', MGREEN),
]
for i, (label, title, sub, desc, border) in enumerate(opts):
    x = Inches(0.8 + i * 4.2)
    rc(s, x, Inches(1.7), Inches(3.8), Inches(5), CDBG, border)
    tx(s, 'OPTION ' + label, x + Inches(0.3), Inches(1.85), Inches(3.2), Inches(0.3), 9, True, border)
    tx(s, title, x + Inches(0.3), Inches(2.3), Inches(3.2), Inches(0.5), 20, True, WHITE)
    tx(s, sub, x + Inches(0.3), Inches(2.9), Inches(3.2), Inches(0.4), 12, True, GOLD)
    tx(s, desc, x + Inches(0.3), Inches(3.6), Inches(3.2), Inches(2.5), 10, False, MUTED)
print('  Slide 9: Partenariat')

# S10 MODELE ECO
s = sl(prs)
sbg(s, DGREEN)
rc(s, Inches(0), Inches(0), W, Inches(0.6), GOLD)
tx(s, 'LES CHIFFRES', Inches(0.5), Inches(0.12), Inches(5), Inches(0.4), 9, True, DGREEN)
tx(s, '08', Inches(12), Inches(0.12), Inches(1), Inches(0.4), 9, False, DGREEN, PP_ALIGN.RIGHT)
tx(s, '500M  >  3 000M+ en 3 ans', Inches(0.8), Inches(0.9), Inches(11), Inches(0.6), 30, True, WHITE)
nums = [('500M', 'Fonds delegues'), ('50 lots', 'x 10M/PME'), ('80%', 'Rendement/12m'), ('900M', 'Retour brut'), ('820M', 'Net FAISE +64%'), ('3000M+', 'Cumule 3 ans')]
for i, (n, l) in enumerate(nums):
    col = i % 3
    row = i // 3
    x = Inches(0.8 + col * 4.2)
    y = Inches(1.8 + row * 2.6)
    rc(s, x, y, Inches(3.8), Inches(2.2), CDBG)
    tx(s, n, x, y + Inches(0.3), Inches(3.8), Inches(0.8), 36, True, GOLD, PP_ALIGN.CENTER)
    tx(s, l, x, y + Inches(1.3), Inches(3.8), Inches(0.4), 11, False, MUTED, PP_ALIGN.CENTER)
rc(s, Inches(0.8), Inches(7.15), Inches(11.7), Inches(0.02), GOLD)
tx(s, 'CUBE x FAISE  |  Cabinet Carree  |  CONFIDENTIEL', Inches(0.8), Inches(7.22), Inches(11), Inches(0.2), 7, False, MUTED)
print('  Slide 10: Modele eco')

# S11 RESULTATS
s = sl(prs)
mhdr(s, 'IMPACT A 3 ANS', '09')
tx(s, 'Diaspora, PME, tissu industriel', Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 26, True, WHITE)
impacts = [
    ('DIASPORA', BLUE, ['500+ investisseurs', '2 Mds FCFA', 'Rendements 50-150%', 'Tracabilite digitale']),
    ('PME', AGREEN, ['100+ financees/an', '+40% CA moyen', 'Stock optimise', 'Bancarisation']),
    ('INDUSTRIEL', GOLD, ['3 secteurs pilotes', 'Expansion UEMOA', 'Creation emplois', 'Contribution PSE']),
]
for i, (title, color, items) in enumerate(impacts):
    x = Inches(0.8 + i * 4.2)
    rc(s, x, Inches(1.7), Inches(3.8), Inches(4.8), CDBG)
    rc(s, x, Inches(1.7), Inches(3.8), Inches(0.06), color)
    tx(s, title, x + Inches(0.3), Inches(1.9), Inches(3.2), Inches(0.4), 14, True, color)
    lines = []
    for it in items:
        lines.append(('> ' + it, 12, False, WHITE))
        lines.append(('', 4, False, None))
    mtx(s, lines, x + Inches(0.3), Inches(2.5), Inches(3.2), Inches(3.5))
print('  Slide 11: Resultats')

# S12 NEXT STEPS
s = sl(prs)
mhdr(s, 'CALENDRIER', '10')
tx(s, 'Demarrons ensemble', Inches(0.8), Inches(0.85), Inches(11), Inches(0.6), 28, True, WHITE)
timeline = [
    ('Avr 2026', 'Protocole d\'accord FAISE x Cabinet Carree'),
    ('Mai 2026', 'Cadre juridique + partenaire bancaire'),
    ('Juin 2026', 'Pilote: 5 PME, 50 investisseurs, 50M FCFA'),
    ('Sept 2026', 'Bilan pilote + ajustements'),
    ('Dec 2026', 'Lancement officiel — Journee Diaspora'),
    ('2027', 'Deploiement + expansion UEMOA'),
]
for i, (date, desc) in enumerate(timeline):
    y = Inches(1.8 + i * 0.8)
    rc(s, Inches(0.8), y + Inches(0.05), Inches(0.15), Inches(0.15), GOLD)
    tx(s, date, Inches(1.2), y, Inches(2), Inches(0.3), 13, True, GOLD)
    tx(s, desc, Inches(3.5), y, Inches(9), Inches(0.3), 13, False, WHITE)
mtx(s, [
    ('', 8, False, None),
    ('Cabinet Carree', 14, True, WHITE),
    ('ccarree.com', 12, False, GOLD),
    ('Dakar, VDN lot 67 Bande Verte, Immeuble Bilguiss', 10, False, MUTED),
], Inches(0.8), Inches(6), Inches(11), Inches(1))
print('  Slide 12: Next Steps')

out = '/home/user/bookish-octo-engine/cube-faise/CUBE_FAISE_Marketing.pptx'
prs.save(out)
import os
print(f'\nMarketing PPTX saved: {out} ({os.path.getsize(out)/1024:.1f} KB)')
