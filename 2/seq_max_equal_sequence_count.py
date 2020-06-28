seq = []

while len(seq) == 0 or seq[-1] != 0:
    seq.append(int(input()))

seq.remove(0)

last = None
counts = []

for n in seq:
    if n == last:
        counts[-1] += 1
        continue

    last = n
    counts.append(1)


print(max(counts))
