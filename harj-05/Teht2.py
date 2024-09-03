luku = "placeholder luku"
lista = []

while luku != "":
    luku = input(f"Syötä luku (lopeta syöttämällä tyhjä): ")

    if luku == "":
        print("Lopetetaan ohjelmaa...")
    else:
        try:
            luku = int(luku)
            lista.append(luku)
        except:
            print(f"Ole ystävällinen ja syötä kokonaisluku!")

lista.sort(reverse=True)
print(f"Viisi suurinta lukua (laskevassa järjestyksessä): {lista[0:5]}")