a = list(map(int, input().split()))

for i in range(len(a) - 1):
    if not i % 2:
        a[i], a[i + 1] = a[i + 1], a[i]

print(*a)
