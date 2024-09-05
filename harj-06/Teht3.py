def muuntaja(bensa):
    litrat = bensa * 3.785
    print(f"{bensa} gallonaa on {litrat} litraa.")

gallonat = float(input(f"Syötä negatiivin luku lopettaaksesi ohjelman. Bensiinin määrä (gallonat): "))
while gallonat >= 0:
    muuntaja(gallonat)
    gallonat = float(input(f"Syötä negatiivin luku lopettaaksesi ohjelman. Bensiinin määrä (gallonat): "))