def paritonkiller(alkup):
    karsittavat = alkup
    print(alkup)
    print(karsittavat)
    for i in karsittavat:
        if i % 2 == 1:
            karsittavat.remove(i)
    return(karsittavat)

lista = []
n = int(input(f"Anna listaan syötettävien lukujen määrä : "))
for i in range(0, n):
    numero = int(input(f"Syötä kokonaisluku listaan: "))
    lista.append(numero)

paritonkiller(lista)

print(lista)
print(paritonkiller(lista))