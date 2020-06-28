timestamp = int(input())
timestamp %= 24 * 60  # дни мы не учитываем

hours = timestamp // 60
minutes = timestamp % 60

print(hours, minutes)
