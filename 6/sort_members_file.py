lines = list(map(lambda x: x.rstrip('\n'),
                 open('input.txt', 'r', encoding='utf8').readlines()))

lines = list(map(lambda line: ' '.join(line.split()[0:2] + line.split()[3::]),
                 lines))

print(*sorted(lines), sep="\n")
