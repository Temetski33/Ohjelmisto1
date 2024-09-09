kuukausinro = int(input(f"Anna kuukauden numero: "))

vuodenajat = ("kevät", "kesä", "syksy", "talvi")

if kuukausinro == 12 or kuukausinro == 1 or kuukausinro == 2:
    print(vuodenajat[3])

elif kuukausinro > 2 and kuukausinro < 6:
    print(vuodenajat[0])

elif kuukausinro > 5 and kuukausinro < 9:
    print(vuodenajat[1])

elif kuukausinro > 8 and kuukausinro < 12:
    print(vuodenajat[2])
