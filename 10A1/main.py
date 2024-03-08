from module import *

jatekosok:list[Jatekos] = []
file = open('juventus.txt', 'r', encoding='utf-8')
for sor in file:
    jatekosok.append(Jatekos(sor))

print(f'f1: igazolt jatekosok szama: {len(jatekosok)} fő')

osszeletkor:int = 0
for j in jatekosok:
    osszeletkor += (2019 - j.szulev)
print(f'f2: atlageletkor: {round(osszeletkor/len(jatekosok), 2)} év')

mini:int = 0
for i in range(1, len(jatekosok)):
    if jatekosok[i].szulev < jatekosok[mini].szulev:
        mini = i
print(f'f3: legidosebb jatekos neve {jatekosok[mini].nev}')

dbhatved:int = 0
for j in jatekosok:
    if j.poszt == 'hátvéd':
        dbhatved += 1
print(f'f4: igazolt jatekosok {dbhatved/len(jatekosok)*100}%-a hátvéd ')

knemzet = input('f5: írjon be egy nemzetiseget: ')
for j in jatekosok:
    if j.nemzetiseg == knemzet:
        print(f'\tVAN {knemzet} nemzetiségű játékos a csapatban')
        break
else: print(f'\tNINCS {knemzet} nemzetiségű játékos a csapatban')