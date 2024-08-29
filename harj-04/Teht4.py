import random

arvaus = 0
vastaus = random.randint(1, 10)

while arvaus != vastaus:
    arvaus = int(input(f"Koitapa arvata luku! :"))
    if arvaus < vastaus:
        print(f"Liian pieni arvaus, häähää!")
    elif arvaus > vastaus:
        print(f"Liian suuri arvaus, hoohoo!")
    elif arvaus == vastaus:
        print(f"Oikein! Onnittelut, voitit pelin!")