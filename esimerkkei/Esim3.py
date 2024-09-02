"""
Erinäistä listasäätöä
"""

nimet = []
lkm = int(input("kuinka monta osallistujaa? "))

#toistetaan nimien kysyminen tarvittava määrä
for i in range(lkm):
    nimi = input("Anna nimi: ")
    #lisätään saatu nimi listan loppuun (append)
    nimet.append(nimi)

#Järjestetään nimet aakkosjärjestykseen.
nimet.sort()
print(f"Nimet aakkosjärjestyksessä:")
print(nimet)

#muokataan listan alkioiden sisältöjä
nimet[1] = "Toka"
nimet[-1] = "Vika"
nimet.insert(0, "Uusi eka")

print(nimet)

#tulostetaan listan alkiot kukin omalla rivillään (for... in).
for alkio in nimet:
    print(alkio)