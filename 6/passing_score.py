lines = list(map(lambda x: x.rstrip('\n'),
                 open('input.txt', 'r', encoding='utf8').readlines()))

# winner = open('output.txt', 'w', encoding='utf8')

scores = list(map(lambda line: list(map(int, line.split()[-3::])), lines))
scores = filter(lambda s: s[0] > 40 and s[1] > 40 and s[2] > 40, scores)

scores = list(map(lambda line: sum(line), list(scores)))

places = int(input())
places_filled = 0

for s in sorted(scores):
    if places_filled + 1 <= places:
        places_filled += 1
    else:
        print(s)
        exit(0)

print(0)
