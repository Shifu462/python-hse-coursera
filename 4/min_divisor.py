def min_divisor(n):
    for num in range(2, int(n ** 0.5) + 1):
        if not n % num:
            return num

    return n


a = int(input())
print(min_divisor(a))
