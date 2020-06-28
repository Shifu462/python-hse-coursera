import sys
from collections import Counter

words = map(str, sys.stdin.read().split())

counter = Counter(words)

for now in sorted(sorted(counter), key=counter.get, reverse=True):
    print(now)
