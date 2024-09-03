"""luku = "placeholder luku"
lista = []

#Tällä hetkellä ohjelma keskeytyy myös syöttämällä 0
while luku != None:
    luku = int(input(f"Syötä luku (lopeta syöttämällä tyhjä): ") or 0)
    luku = luku if luku != 0 else None
    lista.append(luku)

lista.remove(None)
lista.sort(reverse=True)
print(f"Viisi suurinta lukua (laskevassa järjestyksessä): {lista[0:5]}")"""

luku = "placeholder luku"
lista = []

while luku != "":
    luku = input(f"Syötä luku (lopeta syöttämällä tyhjä): ")
    print(luku)

    if luku == "":
        print("tyhjä")
    else:
        print("jotain muuta")
        try:
            luku = int(luku)
            lista.append(luku)
        except:
            print(f"Ole ystävällinen ja syötä kokonaisluku!")

print(luku)
print(lista)
lista.sort(reverse=True)
print(f"Viisi suurinta lukua (laskevassa järjestyksessä): {lista[0:5]}")