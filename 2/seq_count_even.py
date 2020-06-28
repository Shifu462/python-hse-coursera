seq = []

while len(seq) == 0 or seq[-1] != 0:
    seq.append(int(input()))

print(len(list(filter(lambda x: x % 2 == 0, seq))) - 1)
