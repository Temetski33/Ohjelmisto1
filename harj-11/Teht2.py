#Moduuli 10 teht 4

class Auto:
    # matkat alkuarvo
    matkat = [0]
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus
        Auto.matkat.append(self.matka)
        Auto.matkat.sort(reverse=True)

    def tulosta(self):
        print(f"\nAuto {self.rekkari}:")
        print(f"Huippunopeus: {self.huippunopeus}km/h")
        print(f"Nopeus: {self.nopeus}km/h")
        print(f"Kuljettu matka: {self.matka}km")


class Sahkoauto(Auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        print(f"\nRekisterinumero: {self.rekkari} \n"
              f"Huippunopeus: {self.huippunopeus} \n"
              f"Akun kapasiteetti: {self.akkukapasiteetti}")

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, bensatankin_koko):
        self.tankki = bensatankin_koko
        super().__init__(rekkari, huippunopeus)

    def tulosta_tiedot(self):
        print(f"\nRekisterinumero: {self.rekkari} \n"
              f"Huippunopeus: {self.huippunopeus} \n"
              f"Tankin koko: {self.tankki}")


# pääohjelma
sahk = Sahkoauto("ABC-15", 180, 52.5)
polt = Polttomoottoriauto("ACD-123", 165, 32.3)

sahk.kiihdyta(172)
sahk.kulje(3)
sahk.tulosta()

polt.kiihdyta(172)
polt.kulje(3)
polt.tulosta()
