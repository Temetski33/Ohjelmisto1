hytti = input("Kerro laivan hyttiluokka:")

#Toistaiseksi toimii vain jos luokan syöttää isoilla kirjaimilla
if hytti == "LUX":
    print(f"LUX on parvekkeellinen hytti yläkannella.")

elif hytti == "A":
    print(f"A on ikkunallinen hytti autokannen yläpuolella.")

elif hytti == "B":
    print(f"B on ikkunaton hytti autokannen yläpuolella.")

elif hytti == "C":
    print(f"C on ikkunaton hytti autokannen yläpuolella.")

else:
    print(f"Virheellinen hyttiluokka")

#print(f"Testi, hytin luokka on {hytti}.")
