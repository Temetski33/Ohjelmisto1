# Matemattiikka 2 tehtävät 1 tehtävä 4 tehtävä 1

import numpy as np

a = 2.493
b = 0.911

print(f"1.a. \n{a} rad on {np.degrees(a)} astetta.")
print(f"\n1.b. \n{b} rad on {np.degrees(b)} astetta.")

a_kaksi = 137.7
b_kaksi = 62.3

print(f"2.a. \n{a_kaksi} astetta on {np.radians(a_kaksi)} radiaania.")
print(f"\n2.b. \n{b_kaksi} astetta on {np.radians(b_kaksi)} radiaania.")

print(f"\n3.")
Taulukko = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in Taulukko:
    print(f"{i} astetta on {np.radians(i)} radiaania.")

kateetti_a = 1.6
kateetti_b = 2.3

hyponuusa = np.hypot(kateetti_a, kateetti_b)
print(f"\n2.1.\nbHypotenuusa on {hyponuusa}m.")
