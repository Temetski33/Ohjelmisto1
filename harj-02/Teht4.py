#Harjoituksen vuoksi loin ohjelman hyväksymään vain kokonaislukuja inputiksi.

while True:
    try:
        yks = int(input("Anna kolme kokonaislukua. Luku yksi:"))
    except ValueError:
        print("Ole ystävällinen ja syötä kokonaisluku.")
        continue
    break

while True:
    try:
        kaks = int(input("Luku kaksi:"))
    except ValueError:
        print("Ole ystävällinen ja syötä kokonaisluku.")
        continue
    break

while True:
    try:
        kolme = int(input("Luku kolme:"))
    except ValueError:
        print("Ole ystävällinen ja syötä kokonaisluku.")
        continue
    break

summa = yks + kaks + kolme
tulo = yks * kaks * kolme
ka = summa / 3

print(f"Lukujen summa on {summa}.")
print(f"Lukujen tulo on {tulo}.")
print(f"Lukujen keskiarvo on {ka}.")