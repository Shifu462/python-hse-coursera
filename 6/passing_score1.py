inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
scores = (inFile.readlines())
minPP = 40
passing_score = []

for i in range(len(scores)):
    scores[i] = scores[i].split()
    scores[i][-1] = int(scores[i][-1])
    scores[i][-2] = int(scores[i][-2])
    scores[i][-3] = int(scores[i][-3])

for man in scores:
    if man[-1] >= minPP and man[-2] >= minPP and man[-3] >= minPP:
        passing_score.append(man[-3] + man[-2] + man[-1])
passing_score.sort(reverse=1)


if passing_score and len(passing_score) > n:
    while len(passing_score) > n and passing_score[0] != passing_score[-1]:
        passing_score = passing_score[:passing_score.index(min(passing_score))]
    if len(passing_score) > n and passing_score[0] == passing_score[-1]:
        print(1)
    else:
        print(min(passing_score))
else:
    print(0)

inFile.close()
