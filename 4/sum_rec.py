
def sum_recursive(a, b):
    if not b:
        return a

    return sum_recursive(a + 1, b - 1)


print(sum_recursive(int(input()), int(input())))
