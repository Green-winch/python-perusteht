#3.4c Luo ehtolause, jos arvaus on pienempi kuin luku, printtaa "liian pieni". Luo ehtolause, jos arvaus on suurempi kuin luku, printtaa "liian suuri".
import random

luku = random.randint(1, 99)
arvaus = 0

while luku != arvaus:
    print("Arvaa luku:")
    arvaus = int(input())
    
    if arvaus < luku:
        print("Liian pieni")
    elif arvaus > luku:
        print("Liian suuri")
