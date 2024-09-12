def tehtyvalinta():
    valinta = int(input(f"Syötä uusi lentoasema kirjoita 1, hae aseman tiedot kirjoita 2, lopeta kirjoita 3: "))
    if valinta == 0 or valinta >= 4:
        print("Syötevirhe")
    elif 0 < valinta < 4:
        return valinta


def valintafunc():
    tulos = tehtyvalinta()

    if tulos == 1:
        print(f"Syötetään uusi lentoasema.")
        icao = input(f"Syötä aseman ICAO-koodi: ")
        asema = input(f"Syötä aseman nimi: ")
        lentoasemat[icao] = asema
    elif tulos == 2:
        print(f"Haetaan aseman tiedot.")
        haku = input("Anna ICAO-koodi: ")
        if haku in lentoasemat:
            print(f"Koodin {haku} lentoasema on {lentoasemat[haku]}.")
        else:
            print(f"Haetulla koodilla ei löytynyt asemaa.")
    elif tulos == 3:
        print(f"Lopetetaan ohjelma.")
    return tulos

lentoasemat = {}

toistokerroin = 1
while 0 < toistokerroin < 3:
    toistokerroin = valintafunc()