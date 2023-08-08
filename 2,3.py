#2.3 Luo muuttuja, jonka arvoksi asetat random luvun väliltä 0-20. Luo ehto, jos muuttuja on pienempi kuin 5, printtaa "Liian pieni". 
#    Luo ehto, jos muuttuja on suurempi kuin 15, printtaa "Liian suuri". Luo ehto, jos muuttuja on väliltä 5-15, printtaa muuttuja.
import random

pkolikko = input("Kruunu vai klaava?: ")
pkolikko = str(pkolikko)
kolikko = random.randint(0,1)
if kolikko == 0 and pkolikko == "kruunu":
    print("Kruunu")
elif kolikko == 1 and pkolikko == "klaava":
    print("Klaava.")
else:
    print("Arvaa uudelleen.")

