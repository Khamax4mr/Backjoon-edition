from sys import exit

# 세 각 a, b, c 입력.
a = int(input())
b = int(input())
c = int(input())
if a <= 0 or a >= 180: exit(0)
if b <= 0 or b >= 180: exit(0)
if c <= 0 or c >= 180: exit(0)

if a + b + c != 180:
    print('Error')
else:
    match = (a == b) + (b == c) + (a == c)
    if match == 3:
        print('Equilateral')
    elif match == 1:
        print('Isosceles')
    else:
        print('Scalene')