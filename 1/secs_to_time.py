secs = int(input())

secs %= (24 * 60 * 60)  # minus days

hrs = secs // (60 * 60)

secs -= hrs * 60 * 60

mins = secs // 60
secs -= mins * 60

print(f'{hrs}:{mins:02d}:{secs:02d}')
