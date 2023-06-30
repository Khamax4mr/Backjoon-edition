from sys import exit

# 세 각 a, b, c 입력.
a = int(input())
b = int(input())
c = int(input())
if not 0 < a < 180: exit()
if not 0 < b < 180: exit()
if not 0 < c < 180: exit()

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