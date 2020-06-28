from math import gcd

a = int(input())
b = int(input())

while gcd(a, b) != 1.0:
    g = gcd(a, b)
    a //= g
    b //= g

print(a, b)
