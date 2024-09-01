tunnusOikea = "python"
salisOikea = "rules"
counter = 0

tunnus = "placeholder tunnus"
salis = "placeholder salis"

while (tunnus != tunnusOikea or salis != salisOikea) and counter < 5:
    counter = counter + 1
    tunnus = input(f"Kerro tunnus: ")
    salis = input(f"Kerro salis: ")

if counter < 5:
    print(f"Tervetuloa")
else:
    print(f"Pääsy evätty")