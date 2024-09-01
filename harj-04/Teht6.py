#Piin likiarvon laskeminen
#from random import random, randint
#randint(-1, 1)

import random
import math

iterator = 0
N = 1000000
n = 0
while iterator < N:
    iterator += 1
    x = random.random() * 2 - 1
    y = random.uniform(-1, 1)
    print(f"Satunnainen piste: {x}, {y}")
    print(x ** 2 + y ** 2 < 1)
    if  x ** 2 + y ** 2 < 1:
        print(f"Osui ympyrän sisälle.")
        n += 1

print("\n")
print(f"{N} pisteestä {n} osui yksikökympyrän sisälle.")
result = 4 * n / N
print(f"Piin likiarvo on {result}")
print(f"Virhe: {result - math.pi:.5f}")