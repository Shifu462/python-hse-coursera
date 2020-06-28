import sys
from collections import Counter

candidates = filter(lambda x: str.strip(x) != '',
                    map(str, sys.stdin.readlines()))

counter = Counter(candidates)

print(sorted(sorted(counter), key=counter.get, reverse=True)[0])
