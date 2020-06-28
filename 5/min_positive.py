arr = list(map(int, input().split()))

positive = list(filter(lambda x: x > 0, arr))

print(min(positive))
