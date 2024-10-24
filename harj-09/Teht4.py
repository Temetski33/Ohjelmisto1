#Moduuli 9 teht 4

#TEE NOI: lisää kulje .toiminnossa matka listaan
#joka esim auto -luokan sisalla
#ja sorttaa lista ja vertaa suurinta arvoa 10000

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
        #print(f"{self.rekkari} ja {self.huippunopeus}km/h.")
        Auto.lisaa_auto(self)
        Auto.sarja_nro += 1

    def lisaa_auto(self):
        Auto.autot.append(self)
        #print(self.autot)

    def kiihdyta(self):
        self.muutos = random.randint(-10, 15)
        #print(self.muutos)
        self.nopeus = self.nopeus + self.muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus
        #print(self.matka)
        Auto.matkat.append(self.matka)
        Auto.matkat.sort(reverse=True)
        #print(Auto.matkat)
        #print(f"Pisin matka on {Auto.matkat[0]}")

    def tulosta(self):
        print(f"\nAuton {self.rekkari} ominaisuudet:")
        print(f"Huippunopeus: {self.huippunopeus}km/h")
        print(f"Nopeus kisan lopussa: {self.nopeus}km/h")
        print(f"Kuljettu matka: {self.matka}km")


# main
for i in range(10):
    uusiAuto = Auto()

while Auto.matkat[0] < 10000:
    for auto in Auto.autot:
        auto.kiihdyta()

    for auto in Auto.autot:
        auto.kulje(1)

for auto in Auto.autot:
        auto.tulosta()