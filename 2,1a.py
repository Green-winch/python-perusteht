#2.1a Luo kaksi muuttujaa, aseta niille arvoiksi itse haluamasi luvut. Luo ehtolause, jossa vertaat, onko ensimmäinen luku isompi kuin toinen luku. Jos on, niin printtaa "Iso"
import random

luku1 = input("Arvaa numero: ")
luku1 = int(luku1)
luku2 = random.randint(1,41)
if luku1 < luku2:
    print("Liian pieni.")
elif luku1 > luku2:
    print("Liian suuri.")
else:
    print("Voitit.")
