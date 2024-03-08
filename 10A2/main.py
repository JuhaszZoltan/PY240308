from module import *

jatekosok:list[Jatekos] = []
file = open('juventus.txt', 'r', encoding='utf-8')
for s in file: jatekosok.append(Jatekos(s))

print(f'f1: jatekosok szama: {len(jatekosok)} fo')

osszeletkor:int = 0
for j in jatekosok:
    osszeletkor += (2019 - j.ev)
print(f'f2: atlageletkor: {round(osszeletkor / len(jatekosok), 2)} ev')

mini:int = 0
for i in range(1, len(jatekosok)):
    if jatekosok[i].ev < jatekosok[mini].ev:
        mini = i
print(f'f3: legidosebb jatekos: {jatekosok[mini].nev}')

hatveddb:int = 0
for j in jatekosok:
    if j.poszt == 'hátvéd':
        hatveddb += 1
print(f'f4: hatvedek aranya: {hatveddb / len(jatekosok) * 100}%')

kernemzet:str = input('f5: keresett nemzetiseg: ')
for j in jatekosok:
    if j.nemzet == kernemzet:
        print(f'\tVAN {kernemzet} jatekos')
        break
else: print(f'\tNINCS {kernemzet} jatekos')