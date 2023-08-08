#5.1 Mehuvalmistaja tekee mehua sekoitus suhteella 20 % tiivistettä ja 80 % Vettä. Tiiviste maksaa 0.80 €/L ja vesi maksaa 0.05 €/L. Luo sovellus, jolla valmistaja voi helposti laskea mehun hinnan.
#    Valmistaja syöttää sovellukseen mehun määrän litrana ja sovellus palauttaa mehun arvon euroina. Luo toisto lause sovellukseen, jotta kun valmistaja on saanut vastauksen sovellus aloittaa alusta.
def laske_mehun_hinta(maara):
    tiiviste_hintakg = 0.80
    vesi_hintal = 0.05
    tiiviste_osuus = 0.20
    vesi_osuus = 0.80
    hinta = (tiiviste_hintakg * tiiviste_osuus + vesi_hintal * vesi_osuus) * maara
    return hinta

while True:
    mehun_maara = float(input("Syötä mehun määrä litroina (syötä negatiivinen luku lopettaaksesi): "))
    if mehun_maara < 0:
        break
    mehun_hinta = laske_mehun_hinta(mehun_maara)
    print("Mehun hinta:", mehun_hinta, "€")
