kanta = input("Syötä suorakulmion kanta:")
korkeus = input("Syötä suorakulmion korkeus:")

kanta = float(kanta)
korkeus = float(korkeus)

piiri = 2 * kanta + 2 * korkeus
ala = kanta * korkeus

print(f'Suorakulmion ala on {ala}.')
print(f'Suorakulmion piiri on {piiri}.')