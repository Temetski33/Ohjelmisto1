luku = "placeholder luku"
lista = []

while luku != None:
    luku = int(input(f"Syötä luku: ") or 0)
    luku = luku if luku != 0 else None
    lista.append(luku)

lista.remove(None)
lista.sort()
print(f"Pienin syötetty luku on {lista[0]}, suurin syötetty luku on {lista[-1]}")