text = input()
char = 'h'

first_index = text.index(char)
last_index = len(text) - text[::-1].index(char)

print(text[:first_index + 1] +
      text[first_index + 1:last_index - 1] * 2 +
      text[last_index - 1::])
