#2.5b Lisää koodiin ominaisuus, jolla koodi lukee harjoitus.txt tiedoston ja printtaa tiedostossa olleen tekstin.
sana = input("Syötä sana: ")

with open("harjoitus.txt", "w") as tiedosto:
    tiedosto.write(sana)
print("Sana tallennettu tiedostoon harjoitus.txt.")

with open("harjoitus.txt", "r") as tiedosto:
    tiedoston_sisalto = tiedosto.read()
    print("Tiedoston sisältö:")
    print(tiedoston_sisalto)
