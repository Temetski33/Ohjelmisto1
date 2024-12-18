# Periaatteessa kaikki tehtävät 1-3 tässä
# Moduuli 10 teht 3

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin or kohde_kerros < self.alin:
            print(f"Kerrosta ei olemassa.")
            return

        if self.nykyinen_kerros < kohde_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()

        elif self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros == self.ylin:
            print(f"Kerros on jo ylin!")
            return
        self.nykyinen_kerros += 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros == self.alin:
            print(f"Kerros on jo alin!")
            return
        self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")


class Talo:
    hissilista = []
    def __init__(self, alin_nro, ylin_nro, hissi_lkm):
        self.alanro = alin_nro
        self.ylinro = ylin_nro
        self.luo_hissit(hissi_lkm)

    def luo_hissit(self, lkm):
        for nro in range(lkm):
            uus_hissi = Hissi(self.alanro, self.ylinro)
            Talo.hissilista.append(uus_hissi)

    def aja_hissi(self, hissin_nro, kohdekerros):
        ajettava_hissi = self.hissilista[hissin_nro - 1]
        ajettava_hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("Tulipalo! Tulipalo!")
        for hissuli in self.hissilista:
            hissuli.siirry_kerrokseen(self.alanro)


talo1 = Talo(1, 7, 3)
talo1.aja_hissi(1, 5)
talo1.aja_hissi(3, 2)
talo1.palohalytys()
