input()
a = list(map(int, input().split()))
n = int(input())

nearest = None
nearest_abs = None

for i in a:
    if nearest is None or abs(i - n) < nearest_abs:
        nearest = i
        nearest_abs = abs(i - n)

print(nearest)
