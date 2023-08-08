#2.4a Luo muuttuja random luku väliltä 0 -150. Luo ehtolause, jos muuttuja on pienempi kuin 50, niin lisää muuttujan arvoon +50
import random

muuttuja = random.randint(0, 150)
print("Alkuperäinen luku:", muuttuja)
if muuttuja < 50:
    muuttuja += 50
print("Uusi arvo:", muuttuja)
