a, b, c, d, e = int(input()), int(input()), int(input()), \
    int(input()), int(input())

y, n = ("YES", "NO")

if (d >= a and e >= b or
        d >= a and e >= c or
        d >= b and e >= c):
    print(y)
elif (e >= a and d >= b or
        e >= a and d >= c or
        e >= b and d >= c):
    print(y)
else:
    print(n)
