a, b, c, d = float(input()), float(input()), float(input()), float(input())
e, f = float(input()), float(input())

x = (d * e - f * b) / (d * a - b * c)
y = (f * a - e * c) / (d * a - b * c)

print(x, y)
