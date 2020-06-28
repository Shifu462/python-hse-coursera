n = int(input())
true_set = set([i for i in range(1, n + 1)])
false_set = set()
while True:
    guess_set = input()
    if guess_set == 'HELP':
        true_set -= false_set
        break
    resp = input()
    guess_set = set(map(int, guess_set.split()))
    if resp == 'YES':
        true_set &= guess_set
    # elif resp == 'NO':
    else:
        false_set |= guess_set
print(*sorted(true_set))
