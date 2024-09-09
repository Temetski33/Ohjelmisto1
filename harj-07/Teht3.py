#työstö kesken
def tehtyValinta():
    valinta = int(input(f"Syötä uusi lentoasema kirjoita 1, hae aseman tiedot kirjoita 2, lopeta paina 3: "))
    if valinta == 0 or valinta > 4:
        print("Syötevirhe")
    elif 0 < valinta < 4:
        return valinta


def valintafunc():
    tehtyValinta()

    if tehtyValinta == 1:
            print("syöt")
    elif tehtyValinta == 2:
            print("haelol")
    elif tehtyValinta == 3:
        print("lopetataa")

valintafunc()