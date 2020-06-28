y = int(input())
print('YES' if y % 4 == 0 and y % 100 or not y % 400 else 'NO')
