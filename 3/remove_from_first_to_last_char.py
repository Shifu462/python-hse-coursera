def remove_from_first_to_last(text, char):
    first_index = text.index(char)
    last_index = len(text) - text[::-1].index(char)

    first_part = text[0:first_index]
    rest_part = text[last_index::]

    return first_part + rest_part


text = input()

new_text = remove_from_first_to_last(text, 'h')

print(new_text)
