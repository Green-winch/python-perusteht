#4.3a Luo muuttuja panokset ja aseta sen arvoksi 12. Luo funktio nimeltään Ammu, johon syötetään yksi argumentti. 
#     Funktio ammu palauttaa argumentin yhden pienempänä, mutta ei negatiivisena. Jos panoksia vähennettiin, printtaa "Pam" ja printtaa panoksien määrän
panokset = 12

def Ammu(panokset):
    if panokset > 0:
        print("Pam")
        panokset -= 1
    else:
        print("Ei panoksia enää!")
    return panokset
