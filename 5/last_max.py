arr = list(map(int, input().split()))[::-1]

m = max(arr)
i = len(arr) - arr.index(m) - 1

print(m, i)
