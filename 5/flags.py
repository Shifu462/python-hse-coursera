count = int(input())

r = range(1, count + 1)

print('+___ ' * count)

s = ''
for i in r:
    s += f'|{i} / '

print(s)

print('|__\\ ' * count)
print('|    ' * count)

# +___
# |1 /
# |__\
# |
