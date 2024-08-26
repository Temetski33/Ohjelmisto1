vuosi = int(input(f"Kerro vuosiluku:"))
jakoNel = vuosi % 4
jakoSata = vuosi % 100
jakoNelisata = vuosi % 400

if jakoSata == 0 and jakoNelisata == 0:
    print(f"Vuosi on karkausvuosi!")

elif jakoSata == 0 and jakoNelisata != 0:
    print(f"Vuosi ei ole karkausvuosi!")

elif jakoNel == 0:
    print(f"Vuosi on karkausvuosi!")

else:
    print(f"Vuosi ei ole karkausvuosi")


"""print(f"test v {vuosi}")
print(f"test jako {jakoNel}")
print(f"test jako {jakoSata}")
print(f"test jako {jakoNelisata}")"""