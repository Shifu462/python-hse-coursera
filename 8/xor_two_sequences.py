print(*map(lambda pair: int(pair[0] != pair[1]),
           zip(input().split(), input().split())))
