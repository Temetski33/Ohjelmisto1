def summalaskuri(laskettavat):
    summa = sum(laskettavat)
    return(summa)

lista = []
n = int(input(f"Anna listaan syötettävien lukujen määrä : "))
for i in range(0, n):
    numero = int(input(f"Syötä kokonaisluku listaan: "))
    lista.append(numero)

tulos = summalaskuri(lista)
print(f"Listan lukujen summa on {tulos}.")
