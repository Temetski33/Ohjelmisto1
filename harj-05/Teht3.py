luku = int(input(f"Anna kokonaisluku: "))
lista = []
#loppu = luku / 2 + 1

for nro in range(2, luku):
    jaannos = luku % nro
    #print(jaannos)
    lista.append(jaannos)

#print(lista)
if 0 in lista:
    print("Luku ei ole alkuluku!")
else:
    print("Luku on alkuluku!")