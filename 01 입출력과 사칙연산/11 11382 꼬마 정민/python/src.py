# 숫자 a, b, c 입력.
a, b, c = map(int, input().split())
assert 1 <= a <= 10**12
assert 1 <= b <= 10**12
assert 1 <= c <= 10**12

print(a + b + c)