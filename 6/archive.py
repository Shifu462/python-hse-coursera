space, users_count = map(int, input().split())

users = [int(input()) for _ in range(users_count)]

space_filled = 0
users_filled = 0

for u in sorted(users):
    if space_filled + u <= space:
        space_filled += u
        users_filled += 1
    else:
        print(users_filled)
        exit(0)

print(users_filled)
