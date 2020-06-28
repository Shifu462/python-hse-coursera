x = input()
print('0' + (x[x.index('.')::] if '.' in x else ''))
