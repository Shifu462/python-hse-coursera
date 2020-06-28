a = list(map(int, input().split()))

max_idx = a.index(max(a))
min_idx = a.index(min(a))

a[max_idx], a[min_idx] = a[min_idx], a[max_idx]

print(*a)
