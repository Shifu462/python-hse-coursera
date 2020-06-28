text = input()
char = 'f'

first_index = text.index(char) if char in text else None

if first_index is None:
    exit()

print(first_index, end='')

last_index = len(text) - text[::-1].index(char) - 1

if last_index != first_index:
    print(' ' + str(last_index))
