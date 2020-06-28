a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c

if d >= 0 and a != 0:
    r = d ** 0.5
    x = [(-b - r) / (2 * a), (-b + r) / (2 * a)]

    print(*sorted(set(x)))
