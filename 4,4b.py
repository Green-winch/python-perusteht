#4.4b Luo funktio nimeltään Hajoa, joka lisää bugien määrää kertomalla kolmella ja printtaa bugien määrän. Funktio Korjaa tulee kutsua funktio hajoa.
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
