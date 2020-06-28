a = map(int, input().split())
b = map(int, input().split())

print(*sorted(list(set(a) & set(b))))
