from functools import reduce

print(reduce(lambda acc, val: acc * val,
      map(lambda x: int(x) ** 5, input().split())))
