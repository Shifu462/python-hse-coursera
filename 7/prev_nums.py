nums = map(int, input().split())

prev = set()

for i in nums:
    if i in prev:
        print('YES')
    else:
        print('NO')

    prev.add(i)
