#5.4 Luo sovellus, joka generoi satunnaisia nimiä. Sovelluksessa on lista sukunimistä. (keksi nimiä, noin 5kpl on tarpeeksi). 
#    Luo erilliset listat poikien nimistä (noin 5kpl) ja tyttöjen nimistä (noin 5kpl). Sovelluksen tulee olla joustava, eli nimien määrä voi muuttua.
import random

sukunimet = ["Mäkinen", "Virtanen", "Korhonen", "Nieminen", "Koskinen"]
poikien_nimet = ["Elias", "Onni", "Leevi", "Eetu", "Oliver"]
tyttöjen_nimet = ["Emma", "Sofia", "Aino", "Aada", "Veera"]

while True:
    sukupuoli = input("Syötä sukupuoli (poika/tyttö): ")
    if sukupuoli == "poika":
        etunimi = random.choice(poikien_nimet)
    elif sukupuoli == "tyttö":
        etunimi = random.choice(tyttöjen_nimet)
    else:
        print("Virheellinen syöte. Kokeile uudestaan.")
        continue
    
    sukunimi = random.choice(sukunimet)
    print("Satunnainen nimi:", etunimi, sukunimi)
