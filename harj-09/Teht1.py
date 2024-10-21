class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


uusiAuto = Auto("ABC-123", 142)

print(f"Rekkari on {uusiAuto.rekkari:s} ja maksiminopeus {uusiAuto.huippunopeus:d} km/h.")
