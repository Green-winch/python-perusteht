#2.5a Luo muuttuja nimeltään sana ja aseta sen arvoksi käyttäjän syöttämä arvo. Luo tiedosto nimeltään, harjoitus.txt. Aseta koodi kirjoittamaan tiedostoon muuttuja sana.
sana = input("Syötä sana: ")

with open("harjoitus.txt", "w") as tiedosto:
    tiedosto.write(sana)

print("Sana tallennettu tiedostoon harjoitus.txt.")
