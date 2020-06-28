lines = [input().split() for _ in range(int(input()))]

lines = sorted(lines, key=lambda x: int(x[1]), reverse=True)
print(*map(lambda x: x[0], lines), sep='\n')
