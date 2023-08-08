#4.3c Luo while toistolause, jonka ehtona on true. (tarkoituksena toistaa ikuisesti)Toistolauseen tulee kysyä käyttäjältä mitä toimintoa käyttäjä haluaa käyttää. 
#     Jos käyttäjä kirjoittaa ammu, tulee Ammu funktio kutsua. Jos käyttäjä kirjoittaa Lataa, tulee Lataa funktio kutsua.
while True:
    toiminto = input("Kirjoita 'ammu' tai 'lataa': ")
    if toiminto == "ammu":
        panokset = Ammu(panokset)
    elif toiminto == "lataa":
        Lataa()
    else:
        print("Virheellinen komento!")
