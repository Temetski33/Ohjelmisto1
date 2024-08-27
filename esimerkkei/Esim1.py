#While esimerkkejä tunnilta.

"""
hooray_count = int(input(f"Kuinka monta kertaa hurrataan? :"))
hooray_counter = 0
#print(hooray_counter < 3)
while hooray_counter < hooray_count:
    print(f"Jippi jei.")
    hooray_counter = hooray_counter + 1
    print(f"{hooray_counter} kertaa hurraa")

print(f"Hurrattiin {hooray_counter} kertaa ja kivaa oli!")
"""

# komentorivikäyttöliittymä
import random

command = ""
while command != "lopeta":
    command = input("Anna komento> ")
    if command == "tulosta":
        print("Tulostetaan")
    elif command == "lopeta":
        print("Lopetetaan ohjelma.")
        #break # toistorakenteen suoritus loppuu heti!
    elif command == "a":
        print("b")
    elif command == "hurraa":
        hooray_count = int(input(f"Kuinka monta kertaa hurrataan? :"))
        hooray_counter = 0
        # print(hooray_counter < 3)
        while hooray_counter < hooray_count:
            print(f"Jippi jei.")
            hooray_counter = hooray_counter + 1
            print(f"{hooray_counter} kertaa hurraa")

        print(f"Hurrattiin {hooray_counter} kertaa ja kivaa oli!")

    elif command == "noppa":
        noppa1 = noppa2 = heitot = 0
        while (noppa1 != 6 or noppa2 != 6):
            noppa1 = random.randint(1, 6)
            noppa2 = random.randint(1, 6)
            #print(f"Heitit {noppa1} {noppa2}")
            heitot = heitot + 1
        print(f"Tarvittiin {heitot:d} heittoa.")

    else:
        print("Huono komento 0/5")