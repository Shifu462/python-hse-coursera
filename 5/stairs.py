count = int(input())
r = range(1, count + 1)

for row in r:
    print(*range(1, row + 1), sep='')
