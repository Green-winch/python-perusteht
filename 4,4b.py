#4.4b Luo funktio nimeltään Hajoa, joka lisää bugien määrää kertomalla kolmella ja printtaa bugien määrän. Funktio Korjaa tulee kutsua funktio hajoa.
def Hajoa():
    global bugit
    bugit *= 3
    print("Hajosi, bugien määrä:", bugit)
