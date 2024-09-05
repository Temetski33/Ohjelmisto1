import random

def noppaheitto():
    heitto = random.randint(1, 6)
    #print(f"Heitto: {heitto}")
    return(heitto)

tulos = noppaheitto()
while tulos != 6:
    print(f"Heitit: {tulos}")
    tulos = noppaheitto()

print(f"Heitit: {tulos}, onnittelut lopetetaan ohjelma...")