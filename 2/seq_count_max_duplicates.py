seq = []

while len(seq) == 0 or seq[-1] != 0:
    seq.append(int(input()))

first_max = max(seq)
max_duplicates = list(filter(lambda x: x == first_max, seq))

print(len(max_duplicates))
