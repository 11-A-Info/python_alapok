from os import system

system("cls")

# 4. feladat: prog_alapf.5

elsoSzam = int(input("Kérem az első számot: "))
masodikSzam = int(input("Kérem a második számot: "))

logikaiKifejezes_1 = elsoSzam < masodikSzam
logikaiKifejezes_2 = masodikSzam < elsoSzam

if logikaiKifejezes_1:
    kiir = f"A második szám: {masodikSzam} a nagyobb."
    print(kiir)
elif logikaiKifejezes_2:
    kiir = f"Az első szám: {elsoSzam} a nagyobb."
    print(kiir)
else:
    kiir = "A két szám egyenlő."
    print(kiir)
    