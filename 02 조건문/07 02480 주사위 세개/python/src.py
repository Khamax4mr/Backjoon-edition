from sys import exit

# 주사위 눈 a, b, c 입력.
a, b, c = map(int, input().split())
if not 1 <= a <= 6: exit()
if not 1 <= b <= 6: exit()
if not 1 <= c <= 6: exit()

# 상금 계산.
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(100 * max(a, b, c))