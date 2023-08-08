#2.4b Luo ehtolause, jos muuttuja suurempi kuin 100, printtaa "voitit", muulloin printtaa "hävisit".
import random

muuttuja = random.randint(0, 150)
print("Luku:", muuttuja)
if muuttuja > 100:
    print("Voitit!")
else:
    print("Hävisit.")
