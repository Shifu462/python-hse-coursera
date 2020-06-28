n = int(input())

print(*[i ** 2 for i in range(1, n + 1) if i ** 2 <= n])
