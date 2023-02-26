from sys import exit

# 주사위 눈 a, b, c 입력.
a, b, c = map(int, input().split())
if a < 1 or a > 6: exit(0)
if b < 1 or b > 6: exit(0)
if c < 1 or c > 6: exit(0)

# 상금 계산 및 출력.
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(100 * max(a, b, c))