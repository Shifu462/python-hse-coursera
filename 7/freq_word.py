import sys
from collections import Counter

words = map(str, sys.stdin.read().split())

counter = Counter(words)

freqs = counter.most_common(len(counter))

max_count = freqs[0][1]

maxes = map(lambda f: f[0], filter(lambda f: f[1] == max_count, freqs))

maxes = sorted(maxes)

print(maxes[0])
