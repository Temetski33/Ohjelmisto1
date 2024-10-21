class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > 142:
            self.nopeus = 142

        if self.nopeus < 0:
            self.nopeus = 0

        #print(self.nopeus)


uusiAuto = Auto("ABC-123", 142)

print(f"Rekisterinumero {uusiAuto.rekkari:s}, huippunopeus {uusiAuto.huippunopeus:d} km/h.")

uusiAuto.kiihdyta(30)
uusiAuto.kiihdyta(70)
uusiAuto.kiihdyta(50)

print(f"Nopeus on {uusiAuto.nopeus:d} km/h.")

uusiAuto.kiihdyta(-200)

print(f"Nyt nopeus on {uusiAuto.nopeus:d} km/h!")
