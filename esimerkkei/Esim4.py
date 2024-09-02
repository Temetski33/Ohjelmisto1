"""
range-funktio ja for-toisto
"""

print(f"Tulostetaa parilliset luvut väliltä 10 ... 20")


for nro in range(10, 21, 2):
    #huom, alkuarvo 10 kuuluu väliin mutta loppuarvo 21 EI kuulu
    #Kolmas parametri (tässä 2) kertoo lisäyksen määrän
    print(nro)

print(f"Tulostan kaikki luvut väliltä 5 ... 10")
for nro in range(5, 11):
    #lisäyksen oletusarvo on 1
    print(nro)

#Tervehditään 5 kertaa
for nro in range(5):
    print(f"Hei {nro + 1}, kerran")