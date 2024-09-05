def paritonkiller(karsittavat):
    for i in karsittavat:
        if (i % 2 == 1):
            karsittavat.remove(i)
    return(karsittavat)

lista = []
n = int(input(f"Anna listaan syötettävien lukujen määrä : "))
for i in range(0, n):
    numero = int(input(f"Syötä kokonaisluku listaan: "))
    lista.append(numero)

print(lista)
print(paritonkiller(lista))