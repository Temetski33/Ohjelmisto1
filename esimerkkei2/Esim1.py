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
    def __init__(self, name, age, aani = "Mjiuu, mjayy"):
        self.name = name
        self.age = age
        self.omistaja = "Tuntematon"
        self.aani = aani
        # paivitetaan luokkamuuttujan arvo
        Kissa.kissojenLkm += 1

    def tervehdi(self):
        print(self.aani)


# paaohjelma
# luodaan uusi Kissa-tyyppinen olio
ekaKissa = Kissa("Rudolf", 1997)
tokaKissa = Kissa("Giga-Rudolf", 1658, "MJUUUUUR MJAYYYYY")
# tulostetaan kissan arvoja

print(f"{ekaKissa.name:s} on kisuli vuosimallia {ekaKissa.age:d} joka sanoo:")
ekaKissa.tervehdi()

print(f"{tokaKissa.name:s} on kisuli vuosimallia {tokaKissa.age:d} joka sanoo:")
tokaKissa.tervehdi()

print(f"Ja kissojahan on yhteensa {Kissa.kissojenLkm}.")
