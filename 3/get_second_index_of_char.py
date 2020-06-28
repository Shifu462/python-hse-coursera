text = input()
char = 'f'

first_index = text.index(char) if char in text else None

if first_index is None:
    print(-2)
    exit()

second_index = first_index + 1 + text[first_index + 1::].index(char) \
            if char in text[first_index + 1::] \
            else None

result = second_index \
      if second_index is not None \
      else -1

print(result)
