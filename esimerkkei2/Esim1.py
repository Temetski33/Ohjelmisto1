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
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.omistaja = "Tuntematon"

# paaohjelma
# luodaan uusi Kissa-tyyppinen olio
ekaKissa = Kissa("Rudolf", 1997)
# tulostetaan kissan arvoja
print(f"{ekaKissa.name:s} on kisuli vuosimallia {ekaKissa.age:d}.")

#hauska kommentti lolololo