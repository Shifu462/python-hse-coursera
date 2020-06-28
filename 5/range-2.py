a = int(input())
b = int(input())

r = range(a, b + 1)

if b < a:
    r = reversed(range(b, a + 1))

print(*r)
