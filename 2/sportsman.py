km = float(input())
goal = float(input())

day = 1

while km < goal:
    km *= 1.1
    day += 1

print(day)
