seq = []

while len(seq) == 0 or seq[-1] != 0:
    seq.append(int(input()))

first_max = max(seq)
seq[seq.index(first_max)] = 0

print(max(seq))
