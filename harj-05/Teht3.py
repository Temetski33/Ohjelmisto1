import math

luku = int(input(f"Anna kokonaisluku: "))
lista = []
loppu = luku / 2 + 1
loppu = int(math.ceil(loppu))

for nro in range(2, loppu):
    jaannos = luku % nro
    lista.append(jaannos)

if luku < 2:
    print("Luku ei ole alkuluku!")
elif 0 in lista:
    print("Luku ei ole alkuluku!")
else:
    print("Luku on alkuluku!")