#Moduuli 10 teht 4

import random

class Auto:
    sarja_nro = 1
    autot = []
    matkat = [0]
    # matkat listan alku-alkio 0 mahdollistaa loopin toimimisen pääohjelmassa
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
        muutos = random.randint(-10, 15)
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
        print(f"\nAuton {self.rekkari} ominaisuudet:")
        print(f"Huippunopeus: {self.huippunopeus}km/h")
        print(f"Nopeus kisan lopussa: {self.nopeus}km/h")
        print(f"Kuljettu matka: {self.matka}km")


class Kilpailu:
    def __init__(self, kilpailunimi, kilpailukm, kipailuautot):
        self.nimi = kilpailunimi
        self.matka = kilpailukm
        self.kisaajat = kipailuautot
        self.kilpailuaika = 0

    def tunti_kuluu(self):
        for automobiili in self.kisaajat:
            automobiili.kiihdyta()

        for automobiili in self.kisaajat:
            automobiili.kulje(1)

        self.kilpailuaika += 1

        if self.kilpailuaika % 10 == 0:
            self.tulosta_tilanne()

    def tulosta_tilanne(self):
        for automobiili in self.kisaajat:
            automobiili.tulosta()

    def kilpailu_ohi(self):
        if Auto.matkat[0] < self.matka:
            return False

        if Auto.matkat[0] >= self.matka:
            return True

    def aloita_kilpailu(self):
        print(f"{self.nimi} alkakoon!")
        while not Kilpailu.kilpailu_ohi(self):
            self.tunti_kuluu()
        print(f"\nKipailu ohi!")
        self.tulosta_tilanne()


# pääohjelma
for i in range(10):
    uusiAuto = Auto()

suuri_autolista = Auto.autot

kilpailu1 = Kilpailu("Suuri romuralli", 8000, suuri_autolista)
kilpailu1.aloita_kilpailu()
