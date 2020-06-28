def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r


a = IsPointInCircle(float(input()), float(input()),
                    float(input()), float(input()), float(input()))

print("YES" if a else "NO")
