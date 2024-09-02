import random

heittolista = []
lukum = int(input(f"Anna noppien lukumäärä: "))

for nro in range(lukum):
    heitto = random.randint(1, 6)
    heittolista.append(heitto)

summa = sum(heittolista)
print(f"Silmälukujen summa on yhteensä {summa}")