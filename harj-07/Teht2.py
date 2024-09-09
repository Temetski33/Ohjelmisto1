nimi = "placeholderLOLOLOLOLO"
nimijoukko = set()

while nimi != "":
    nimi = input("Anna nimi: ")
    print(nimi)
    if nimi in nimijoukko:
        nimijoukko.add(nimi)
        print("Aiemmin syötetty nimi")
    else:
        nimijoukko.add(nimi)
        print("Uusi nimi")

print(*nimijoukko, sep = "\n")