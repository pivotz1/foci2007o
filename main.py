'''
A 2007-es októberi emelt informatika érettségi feladata (Foci)
'''
meccsek = []

# region 1. feladat
f = open("meccs.txt", "r")
f.readline()  # első sor nem kell!
sor = f.readline()  # ez az első "értékes" sor
while sor:
    sor = sor.strip().split()
    meccs = {
        'fordulo': int(sor[0]),
        'hazaigol': int(sor[1]),
        'vendeggol': int(sor[2]),
        '1felido': int(sor[3]),
        '2felido': int(sor[4]),
        'hazaicsapat': sor[5],
        'vendegcsapat': sor[6]
    }
    meccsek.append(meccs)
    sor = f.readline()
f.close()
# endregion

# region 2. feladat
fordulokszama = max(map(lambda m: m['fordulo'], meccsek))
fordulo = int(input(f"2. feladat: Kérem a forduló számát [1..{fordulokszama}]: "))
for m in meccsek:
    if m['fordulo'] == fordulo:
        print("\t{0}-{1}: {2}-{3} ({4}-{5})".format(m['hazaicsapat'], m['vendegcsapat'], m['hazaigol'],
                                                    m['vendeggol'], m['1felido'], m['2felido']))
# endregion

# region 3. feladat
print("3. feladat: (akik fordítani tudtak)")
for m in meccsek:
    if (m['hazaigol'] > m['vendeggol'] and m['1felido'] < m['2felido']) or (
            m['hazaigol'] < m['vendeggol'] and m['1felido'] > m['2felido']):
        print("\t{0}: {1}".format(m['fordulo'], m['hazaicsapat'] if m['hazaigol'] > m['vendeggol'] else m['vendegcsapat']))
# endregion

# region 4. feladat
# ez ugyan nem a feladat része, de elegánsabb, ha csak létező csapatneveket fodagunk el:
hcsapatok = set(map(lambda m: m['hazaicsapat'].lower(), meccsek))
vcsapatok = set(map(lambda m: m['vendegcsapat'].lower(), meccsek))
csapatok = list(set(list(hcsapatok) + list(vcsapatok)))    # halmazba (lista-halmaz-lista)!
csapat = input("4. feladat: Kérek egy csapatnevet: ")
while csapat.lower() not in csapatok:
    csapat = input("4. feladat: Kérek egy csapatnevet: ")
# endregion

# region 5. feladat
lottgol = 0
kapottgol = 0
for m in meccsek:
    if m['hazaicsapat'].lower() == csapat.lower():
        lottgol += m['hazaigol']
        kapottgol += m['vendeggol']
    if m['vendegcsapat'].lower() == csapat.lower():
        lottgol += m['vendeggol']
        kapottgol += m['hazaigol']
print(f"5. feladat: A(z) {csapat} csapat góljai:")
print(f"\t  Lőtt gólok: {lottgol}")
print(f"\tKapott gólok: {kapottgol}")
# endregion

# region 6. feladat
i = 0
while i < len(meccsek):
    if meccsek[i]['hazaicsapat'].lower() == csapat.lower() and meccsek[i]['hazaigol'] < meccsek[i]['vendeggol']:
        print("6. feladat: A(z) {0} csapat először a {1} fordulóban kapott ki a {2} csapattól".
              format(csapat, meccsek[i]['fordulo'], meccsek[i]['vendegcsapat']))
        break
    i += 1
if i == len(csapatok):
    print("6. feladat: A(z) {0} csapat otthon veretlen maradt.")
# endregion

# region 7. feladat
from itertools import groupby

# először a góleredmények alapján történő csoportosítás (hazaigólok-vendéggólok):
allasok = groupby(sorted(meccsek, key=lambda m: str(m['hazaigol']) + '-' + str(m['vendeggol'])),
                  key=lambda m: str(m['hazaigol']) + '-' + str(m['vendeggol']))
# most a statisztika készítése, a fordított eredmények azonosnak vételével:
stat = {}
for allas, db in allasok:                       # mivel a csoportosításhoz már állások szerinti növekvő sorban van,
    if allas[::-1] in stat:                     # ha a fordítottja már benne lenne a szótárban...
        stat[allas[::-1]] += len(list(db))      # ...akkor hozzáadjuk ahhoz az ilyenek darabszámát is
    else:
        stat.setdefault(allas, len(list(db)))   # ha az állás még nincs benne, akkor beletesszük a darabszámmal együtt
print("7. feladat: Végeredmény-statisztika:")
for e in stat:
    print(f"\t{e}: {stat[e]} darab")
# endregion
