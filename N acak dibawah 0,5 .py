from random import random

angka_acak = []

while len(angka_acak) < 5:
    for _ in range(1):
        n = random()
        if n < 0.5:
            angka_acak.append(n)
            print(n)
