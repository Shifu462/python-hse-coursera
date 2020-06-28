def IsPointInSquare(x, y):
    return x >= -1 and x <= 1\
        and y >= -1 and y <= 1


print("YES" if IsPointInSquare(float(input()), float(input())) else "NO")
