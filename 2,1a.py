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