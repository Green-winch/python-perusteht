#5.3 Luo sovellus, joka laskee harjoittelun määrän. Sovellukseen syötetään harjoittelun määrä/pv. Sovellus printtaa määrän, jonka käyttäjä harjoittelee vuodessa tunteina. 
#    Sovellus printtaa myös määrän (päivinä), jonka käyttäjän tulee harjoitella tullakseen mestariksi (10 000h).

def laske_vuoden_harjoittelu(paivittainen_harjoittelu):
    vuoden_tunnit = paivittainen_harjoittelu * 365
    return vuoden_tunnit

while True:
    harjoitus_maara = float(input("Syötä päivittäinen harjoittelumäärä tunteina (syötä negatiivinen luku lopettaaksesi): "))
    if harjoitus_maara < 0:
        break
    vuoden_tunnit = laske_vuoden_harjoittelu(harjoitus_maara)
    print("Vuodessa harjoittelet:", vuoden_tunnit, "tuntia")
    mestariksi_tarvittavat_tunnit = 10000
    paivina = mestariksi_tarvittavat_tunnit / harjoitus_maara
    print("Mestariksi tulemiseen tarvitaan", paivina, "päivää")
