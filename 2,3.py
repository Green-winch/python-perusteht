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

