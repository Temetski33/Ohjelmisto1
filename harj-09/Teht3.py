# Tässä käytännössä moduulin kaikki tehtävät 1-3.

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 2000

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus


uusiAuto = Auto("ABC-123", 142)

print(f"Rekisterinumero {uusiAuto.rekkari:s}, huippunopeus {uusiAuto.huippunopeus:d} km/h.")

uusiAuto.kiihdyta(30)
uusiAuto.kiihdyta(70)
uusiAuto.kiihdyta(50)

print(f"Nopeus on {uusiAuto.nopeus:d} km/h.")

uusiAuto.kiihdyta(-200)

print(f"Nyt nopeus on {uusiAuto.nopeus:d} km/h!")

uusiAuto.kiihdyta(60)
uusiAuto.kulje(1.5)
print(f"Kuljettu matka on {uusiAuto.matka:f} km.")
