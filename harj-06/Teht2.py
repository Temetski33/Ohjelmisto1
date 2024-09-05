import random

def noppaheitto(tahkot):
    heitto = random.randint(1, tahkot)
    #print(f"Heitto: {heitto}")
    return(heitto)

tahkotSyote = int(input(f"Syötä tahkojen määrä: "))
tulos = noppaheitto(tahkotSyote)
while tulos != tahkotSyote:
    print(f"Heitit: {tulos}")
    tulos = noppaheitto(tahkotSyote)

print(f"Heitit: {tulos}, joka on sama kuin tahkojen määrä.")