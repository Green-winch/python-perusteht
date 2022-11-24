import random

pkolikko = input("Kruunu vai klaava?: ")
pkolikko = str(pkolikko)
kruunu = 0
klaava = 1
if pkolikko == 0:
    print("Kruunu")
elif pkolikko == 1:
    print("Klaava.")
else:
    print("Arvasit väärin.")
    
