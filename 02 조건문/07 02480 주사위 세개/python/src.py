# 주사위 눈 a, b, c 입력.
a, b, c = map(int, input().split())
assert 1 <= a <= 6
assert 1 <= b <= 6
assert 1 <= c <= 6

# 상금 계산.
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(100 * max(a, b, c))