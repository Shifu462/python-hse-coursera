import sys
words = map(str, sys.stdin.read().split())

counts = {}

results = []

for w in words:
    if w in counts:
        results.append(counts[w])
    else:
        results.append(0)
        counts[w] = 0

    counts[w] += 1

print(*results)
