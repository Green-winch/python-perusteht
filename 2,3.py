#2.3 Luo muuttuja, jonka arvoksi asetat random luvun väliltä 0-20. Luo ehto, jos muuttuja on pienempi kuin 5, printtaa "Liian pieni". 
#    Luo ehto, jos muuttuja on suurempi kuin 15, printtaa "Liian suuri". Luo ehto, jos muuttuja on väliltä 5-15, printtaa muuttuja.
import random

kolikko = random.randint(0, 20)
if kolikko < 5:
    print("Liian pieni")
elif kolikko > 15:
    print("Liian suuri")
else:
    print(kolikko)
