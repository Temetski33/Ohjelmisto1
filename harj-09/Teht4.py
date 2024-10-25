#Moduuli 9 teht 4

import random

class Auto:
    sarja_nro = 1
    autot = []
    matkat = [0]
    # matkat listan alku-alkio 0 mahdollistaa while loopin toimimisen paaohjelmassa
    def __init__(self):
        self.rekkari = f"ABC-{Auto.sarja_nro}"
        self.huippunopeus = random.randint(100, 200)
        self.nopeus = 0
        self.matka = 0
        Auto.lisaa_auto(self)
        Auto.sarja_nro += 1

    def lisaa_auto(self):
        Auto.autot.append(self)

    def kiihdyta(self):
        self.muutos = random.randint(-10, 15)
        self.nopeus = self.nopeus + self.muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus
        Auto.matkat.append(self.matka)
        Auto.matkat.sort(reverse=True)

    def tulosta(self):
        print(f"\nAuton {self.rekkari} ominaisuudet:")
        print(f"Huippunopeus: {self.huippunopeus}km/h")
        print(f"Nopeus kisan lopussa: {self.nopeus}km/h")
        print(f"Kuljettu matka: {self.matka}km")


# main ohjelma
for i in range(10):
    uusiAuto = Auto()

while Auto.matkat[0] < 10000:
    for auto in Auto.autot:
        auto.kiihdyta()

    for auto in Auto.autot:
        auto.kulje(1)

for auto in Auto.autot:
        auto.tulosta()