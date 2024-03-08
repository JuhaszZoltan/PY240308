from module import *

termekek:list[Termek] = []
file = open('vm.txt', 'r', encoding='utf-8')
for s in file: termekek.append(Termek(s))

print(f'f1: termekek szama: {len(termekek)} db')

mini:int = 0
for i in range(1, len(termekek)):
    if termekek[i].ar < termekek[mini].ar:
        mini = i
print(f'f2: legolcsobb termek: {termekek[mini].nev} ({termekek[mini].ar} HUF)')

osszes_ml:int = 0
for t in termekek:
    if 'ml' in t.nev:
        osszes_ml += (t.kiszereles * t.keszlet)
print(f'f3: osszes folyadek: {osszes_ml / 1000} liter')

bevetel:int = 0
for t in termekek:
    bevetel += (12 - t.keszlet) * t.ar
print(f'osszes bevetel: {bevetel} HUF')