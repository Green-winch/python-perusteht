#3.2b Lisää toistolauseeseen ehtolause: Jos silakat <= 0, niin printtaa "Pitää ostaa lisää".
silakat = 10
while silakat > 0:
    print("Silakoita:", silakat)
    silakat -= 1
    if silakat <= 0:
        print("Pitää ostaa lisää")
