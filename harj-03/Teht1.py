kuha = int(input(f"Anna kuhan mitta senttimetrin tarkkuudella:"))
alimitta = 37 - kuha

if alimitta > 0:
    print(f"Kuha on {alimitta} cm alamittainen! Laske se takaisin järveen!")

else:
    print(f"On komea kuha!")