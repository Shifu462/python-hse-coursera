n = input()

if '.' not in n:
    print(n)
    exit()

s = n.split('.')
i = s[0]
f = s[1]

print(i if int(f[0]) < 5 else int(i) + 1)
