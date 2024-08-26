sukup = input(f"Kerro sukupuolesi (mies/nainen):")
hemo = int(input(f"Kerro hemoglobiini arvosi (g/l):"))

if sukup == "mies" and hemo < 134:
    print(f"Hemoglobiiniarvosi on alhainen.")

elif sukup == "mies" and 134 <= hemo <= 195:
    print(f"Hemoglobiiniarvosi on normaali.")

elif sukup == "mies" and hemo > 195:
    print("Hemoglobiiniarvosi on korkea.")

elif sukup == "nainen" and hemo < 117:
    print(f"Hemoglobiiniarvosi on alhainen.")

elif sukup == "nainen" and 117 <= hemo <= 175:
    print("Hemoglobiiniarvosi on normaali.")

elif sukup == "nainen" and hemo > 175:
    print("Hemoglobiiniarvosi on korkea.")

else:
    print("Virhe tietoja syöttäessä. Syötä uudestaan.")
