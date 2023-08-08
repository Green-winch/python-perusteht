#5.2 Luo sovellus, joka laskee etäisyyksiä. Sovelluksessa tulee olla funktio, joka antaa käyttäjän syöttää uudet koordinaatti arvot. 
#    Sovelluksessa tulee olla funktio, joka laskee etäisyyden koordinaattien välillä. Etäisyys lasketaan d = √((P2x-P1x)² + (P2y-P1y)²).
import math

def laske_etaisyys(x1, y1, x2, y2):
    etaisyys = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return etaisyys

while True:
    x1 = float(input("Syötä ensimmäisen pisteen x-koordinaatti: "))
    y1 = float(input("Syötä ensimmäisen pisteen y-koordinaatti: "))
    x2 = float(input("Syötä toisen pisteen x-koordinaatti: "))
    y2 = float(input("Syötä toisen pisteen y-koordinaatti: "))
    etaisyys = laske_etaisyys(x1, y1, x2, y2)
    print("Etäisyys:", etaisyys)
