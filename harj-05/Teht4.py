nimet = []
lkm = 5

#toistetaan nimien kysyminen tarvittava määrä
for i in range(lkm):
    nimi = input("Anna nimi: ")
    #lisätään saatu nimi listan loppuun (append)
    nimet.append(nimi)

for i in range(lkm):
    print(nimet[i])