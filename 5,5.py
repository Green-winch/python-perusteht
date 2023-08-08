#5.5 Luo sovellus, joka laskee lenkkeilyn määrän. Sovellus kertoo lenkkeillyn määrän kilometreinä. Käyttäjä syöttää sovellukseen liikutun määrän. 
#    Liikuttumäärä tallennetaan tiedostoon. Sovellus antaa käyttäjän nähdä liikutun määrän ja lisätä määrää.

def tallenna_liikutut_km(liikutut_km):
    with open("liikutut_km.txt", "a") as tiedosto:
        tiedosto.write(str(liikutut_km) + "\n")

def nayta_liikutut_km():
    try:
        with open("liikutut_km.txt", "r") as tiedosto
