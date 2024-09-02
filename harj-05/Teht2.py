luku = "placeholder luku"
lista = []

while luku != None:
    luku = int(input(f"Syötä luku (lopeta syöttämällä tyhjä): ") or 0)
    luku = luku if luku != 0 else None
    lista.append(luku)

lista.remove(None)
lista.sort(reverse=True)
print(f"Viisi suurinta lukua (laskevassa järjestyksessä): {lista[0:5]}")