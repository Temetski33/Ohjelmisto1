"""class Koira:
    pass


koira = Koira()
koira.nimi = "Rekku"
koira.syntymavuosi = 2022

print(f"{koira.nimi:s} on syntynyt vuonna {koira.syntymavuosi:d}.")"""

"""class Koira:
    def __init__(self, nimi, syntymavuosi):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi

koira = Koira("Rekku", 2022)

print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymavuosi:d}." )"""

# maaritellaan Kissa-luokka

class Kissa:
    # luokkamuuttuja, kaikille olioille yhteinen
    kissojenLkm = 0

    # luokan alustaja
    def __init__(self, name, age, aani = "Mjiuu, mjayy", omistaja =None):
        self.name = name
        self.age = age
        # omistaja on viittaus Omistaja luokasta luotuun olioon
        self.omistaja = omistaja
        # kaytetaan viittausta Omistaja-olioon, ja lisataan nyt luotava
        # kissa jotain jotain
        omistaja.lisaa_kissa(self)
        self.aani = aani
        # paivitetaan luokkamuuttujan arvo
        Kissa.kissojenLkm += 1

    # maaritellaan oliolle toiminto eli metodi
    def tervehdi(self):
        print(f"\n{self.aani}! Olen {self.name}.")
        print(f"Olen jo {self.age} vuotta vanha. Omistajani on {self.omistaja.nimi}.")


class Omistaja:
    def __init__(self, nimi, puh="tuntematon"):
        self.nimi = nimi
        self.puh = puh
        self.kissat = []

    def lisaa_kissa(self, kissa):
        # estetaan saman kissan paatyminen listalle kahteen kertaan
        for k in self.kissat:
            if k == kissa:
                return
        self.kissat.append(kissa)

    def esittele(self):
        print(f"Olen {self.nimi}, puh: {self.puh}.")
        print(f"Omistan kissat:")
        for cat in self.kissat:
            print(f"{cat.name}, ikä: {cat.age}")


# paaohjelma
viivi = Omistaja("Viivi Vihanto", "040 1234666")

# luodaan uusi Kissa-tyyppinen olio
ekaKissa = Kissa("Rudolf", 2, omistaja=viivi)
tokaKissa = Kissa("Giga-Rudolf", 658, "MJUUUUUR MJAYYYYY", viivi)


"""ekaKissa.tervehdi()
tokaKissa.tervehdi()"""

# Kissa -luokka tekee jo alla olevan
"""viivi.lisaa_kissa(ekaKissa)
viivi.lisaa_kissa(ekaKissa)
viivi.lisaa_kissa(tokaKissa)"""

viivi.esittele()

# laitetaan kaikki Viiviv kissat esittelemaan itsensa
for kissa in viivi.kissat:
    kissa.tervehdi()


"""# luodaan 5 kissaa lisaa
kisulista = []
for i in range(5):
    uus_kissa = Kissa(f"Cat name {i}", i, f"Moro {i}")
    kisulista.append(uus_kissa)

#kaikki uudet kissat tervehtii
for kisu in kisulista:
    kisu.tervehdi()"""

print(f"\nJa kissojahan on yhteensa {Kissa.kissojenLkm}.")
