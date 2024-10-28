class Koira:

    def __init__(self, nimi, tervehdys="vuh vuh!"):
        self.nimi = nimi
        self.tervehdys = tervehdys

    def tervehdi(self):
        print(self.tervehdys)


class RotuKoira(Koira):

    def __init__(self, nimi, rotu, tervehdys="vuh vuh!"):
        super().__init__(nimi, tervehdys)
        self.rotu = rotu

    def tervehdi(self):
        print(f"{self.tervehdys}, ich bin eine {self.rotu}. Good evening.")


koiraA = Koira("Ressu")
hieno_koira = RotuKoira("Mr Bean", "beagle")

koiraA.tervehdi()
hieno_koira.tervehdi()