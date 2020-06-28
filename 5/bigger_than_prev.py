arr = list(map(int, input().split()))

b = []
for i in range(1, len(arr)):
    if arr[i - 1] < arr[i]:
        b.append(arr[i])

print(*b)
