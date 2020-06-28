import sys

print(len(set((lambda y: (' '.join(y)).split())(list(sys.stdin)))))
