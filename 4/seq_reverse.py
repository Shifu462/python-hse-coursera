seq = []

a = None
while len(seq) == 0 or seq[-1] != 0:
    seq.append(int(input()))

r = reversed(seq)

print(*r, sep="\n")
