from sys import exit

while True:
    # 세 변의 길이 a, b, c 입력.
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0: break
    if a <= 0 or a > 1000: exit(0)
    if b <= 0 or b > 1000: exit(0)
    if c <= 0 or c > 1000: exit(0)

    if a + b <= c or b + c <= a or a + c <= b:
        print('Invalid')
    else:
        match = (a == b) + (b == c) + (c == a)
        if match == 3:
            print('Equilateral')
        elif match == 1:
            print('Isosceles')
        else:
            print('Scalene')