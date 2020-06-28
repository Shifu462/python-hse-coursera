seq = []

while len(seq) == 0 or seq[-1] != 0:
    seq.append(int(input()))

print(sum(seq))
