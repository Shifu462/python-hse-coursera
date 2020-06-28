a, b, c = float(input()), float(input()), float(input())

half_P = (a + b + c) / 2

area = (half_P * (half_P - a) * (half_P - b) * (half_P - c)) ** 0.5

print(area)
