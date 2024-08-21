leiv = input("Anna leiviskät:")
naul = input("Anna naulat:")
luot = input("Anna luodit:")

leiv = float(leiv)
naul = float(naul)
luot = float(luot)

LuoditYht = 20 * 32 * leiv + 320 * naul + luot
Grammat = 13.3 * LuoditYht
Nykymassa = Grammat

print(f'Massa grammoina on {Grammat}.')
print(f'Massa nykymittojen mukaan on {Nykymassa}.')