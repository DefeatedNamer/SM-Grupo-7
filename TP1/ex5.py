import math
from random import randint

bitSequence = [0] * 16
y = 0

while y < len(bitSequence):
    bitSequence[y] = randint(0, 1)
    y += 1

numberOf1s = bitSequence.count(1)

print(f"Sequence: {bitSequence}")
print(f"Number of 1's: {numberOf1s}")


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


entropy1o = 0
x = 0

while x < 17:
    entropy1o -= (nCr(16, x) / 2 ** 16) * math.log((nCr(16, x) / 2 ** 16), 2)
    x += 1

print(f"Entropy: {entropy1o}")
