#Mod 11 Teht 1

class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjailija, sivut):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivut = sivut

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}. Kirjailija {self.kirjailija}, pituus {self.sivut} sivua.")

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}. Paatoimittaja {self.paatoimittaja}.")


# main
aku = Lehti("Aku Ankka", "Aki Hyyppa")
hytti = Kirja("Hytti nro 6", "Rosa Liksom", 200)
aku.tulosta_tiedot()
hytti.tulosta_tiedot()
