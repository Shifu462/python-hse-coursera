a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

p = ''

if a1 > b1:
    (b1, a1) = (a1, b1)

if b1 > c1:
    (b1, c1) = (c1, b1)

if a1 > b1:
    (a1, b1) = (b1, a1)

if a2 > b2:
    (b2, a2) = (a2, b2)

if b2 > c2:
    (b2, c2) = (c2, b2)

if a2 > b2:
    (a2, b2) = (b2, a2)

if a1 == a2 and b1 == b2 and c1 == c2:
    p = 'Boxes are equal'

elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    p = 'The first box is smaller than the second one'

elif b2 <= b1 and a2 <= a1 and c2 <= c1:
    p = 'The first box is larger than the second one'

else:
    p = 'Boxes are incomparable'

print(p)
