input_file = open("input.txt", encoding='utf8')
candidates = {}
votes = 0
for line in input_file:
    candidate = line.strip()
    candidates[candidate] = candidates.get(candidate, 0) + 1
    votes += 1

maximal = max(candidates, key=candidates.get)
output_file = open('output.txt', 'w', encoding='utf8')
if 2 * candidates[maximal] > votes:
    print(maximal, file=output_file)
else:
    print(maximal, file=output_file)
    print(sorted(candidates, key=candidates.get, reverse=True)[1],
          file=output_file)
