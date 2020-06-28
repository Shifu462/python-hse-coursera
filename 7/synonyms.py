d = dict()

n = int(input())

for _ in range(n):
    [word, trans] = input().split()
    d[word] = trans

inv = {v: k for k, v in d.items()}

w = input()

print(d[w] if w in d.keys() else inv[w])
