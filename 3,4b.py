#3.4b Luo while toistolause, jonka ehtona on, että luku ja arvaus ovat erisuuret. Lisää toistolauseeseen printtaus: "arvaa luku". Aseta muuttujan arvaus arvoksi käyttäjän syöttämä luku.
while luku != arvaus:
    print("Arvaa luku:")
    arvaus = int(input())
    if arvaus < luku:
        print("Liian pieni")
    elif arvaus > luku:
        print("Liian suuri")
