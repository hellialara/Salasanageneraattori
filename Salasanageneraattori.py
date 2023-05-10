from random import choice 
import string

print("Tervetuloa salasanageneraattorin pariin!")
while True:
    try:
        pituus = int(input("Anna salasanan pituus (8-24 merkkiä): "))
    except ValueError:
        print("Käytä numeroita ja yritä uudestaan")
        continue
    if pituus < 8:
        print("Liian lyhyt. Yritä uudestaan")
    elif pituus > 24:
        print("Liian pitkä. Yritä uudestaan")
    else:
        break

while True:
    isot = input("Haluatko mukaan isoja kirjaimia? (y/n): ")
    if isot == "y" or isot == "n":
        break
    else:
        print("En ymmärrä. Yritä uudestaan!")

while True:          
    numerot = input("Haluatko mukaan numeroita? (y/n): ")
    if isot == "y" or isot == "n":
        break
    else:
        print("En ymmärrä. Yritä uudestaan!")

while True:          
    erikoismerkit = input("Haluatko mukaan erikoismerkkejä? (y/n): ")
    if isot == "y" or isot == "n":
        break
    else:
        print("En ymmärrä. Yritä uudestaan!")

salasana = ""
merkit_mukaan = string.ascii_lowercase
isot_kirjaimet = string.ascii_uppercase
numerolista = "0123456789"
merkkilista = "!#¤%&/()=?"

if isot == "y":
    merkit_mukaan += isot_kirjaimet

if numerot == "y":
    merkit_mukaan += numerolista

if erikoismerkit == "y":
    merkit_mukaan += merkkilista


for i in range(pituus):
    salasana += choice(merkit_mukaan)

print(salasana)


