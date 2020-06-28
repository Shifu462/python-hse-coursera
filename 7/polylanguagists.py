input_file = open('input.txt', 'r', encoding='utf8')
n = int(input_file.readline())
N = set()
R = set()
m = int(input_file.readline())
M = set()
for langueges in range(m):
    M.add(input_file.readline().strip())
N |= M
R |= M
for now in range(n - 1):
    m = int(input_file.readline())
    M = set()
    for langueges in range(m):
        M.add(input_file.readline().strip())
    N |= M
    R &= M
print(len(R))
print(*R, sep='\n')
print(len(N))
print(*N, sep='\n')
