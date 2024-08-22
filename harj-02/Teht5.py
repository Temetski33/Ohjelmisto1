import math
leiv = input("Anna leiviskät:")
naul = input("Anna naulat:")
luot = input("Anna luodit:")

leiv = float(leiv)
naul = float(naul)
luot = float(luot)

LuoditYht = 20 * 32 * leiv + 320 * naul + luot
Grammat = 13.3 * LuoditYht
Nykymassa = Grammat / 1000
Kilomassa = math.trunc(Nykymassa)
GrammatDesimaali = Grammat % 1000

print(Grammat)
print(f"Ja viimein {Kilomassa} kilogrammaa ja {GrammatDesimaali:3.2f} grammaa.")