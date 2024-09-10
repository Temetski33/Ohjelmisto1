#työstö kesken
def tehtyvalinta():
    valinta = int(input(f"Syötä uusi lentoasema kirjoita 1, hae aseman tiedot kirjoita 2, lopeta kirjoita 3: "))
    if valinta == 0 or valinta > 4:
        print("Syötevirhe")
    elif 0 < valinta < 4:
        return valinta


def valintafunc():
    tulos = tehtyvalinta()

    if tulos == 1:
        print("syöt")
    elif tulos == 2:
        print("haelol")
    elif tulos == 3:
        print("lopetataa")

valintafunc()
