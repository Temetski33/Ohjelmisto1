import math

def pizzalaskuri(halkaisija, hinta):
    halkaisijametreina = halkaisija / 100
    sade = halkaisijametreina / 2
    ala = math.pi * sade ** 2
    squareprice = hinta / ala
    return(squareprice)

pizza1d = float(input("Syötä pizzan 1 halkaisija (cm): "))
pizza1e = float(input("Syötä pizzan 1 hinta (€): "))
pizza2d = float(input("Syötä pizzan 2 halkaisija (cm): "))
pizza2e = float(input("Syötä pizzan 2 hinta (€): "))

squareprice1 = pizzalaskuri(pizza1d, pizza1e)
squareprice2 = pizzalaskuri(pizza2d, pizza2e)

#Alla neliöhinnan testailua
print(f"test p1 {squareprice1:.1f} test p2 {squareprice2:.1f}")

if squareprice1 < squareprice2:
    print(f"Pizza 1 antaa paremman vastineen rahalle.")
elif squareprice1 > squareprice2:
    print(f"Pizza 2 antaa paremman vastineen rahalle.")
else:
    print(f"Molemmat pizzat antavat saman vastineen rahalle.")