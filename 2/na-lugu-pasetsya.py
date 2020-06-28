n = int(input())
last = n % 10

choice = 'korov' if last >= 5 or last == 0 or n in range(5, 20)\
    else 'korovy' if last in [2, 3, 4]\
    else 'korova'

print(f'{n} {choice}')
