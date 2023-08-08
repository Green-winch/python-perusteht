#4.4a Luo muuttuja bugit ja aseta sen arvoksi 2. Luo funktio nimeltään Korjaa, joka vähentää bugien määrää yhdellä ja printtaa bugien määrän.
bugit = 2

def Korjaa():
    global bugit
    bugit -= 1
    print("Korjattu, bugien määrä:", bugit)
