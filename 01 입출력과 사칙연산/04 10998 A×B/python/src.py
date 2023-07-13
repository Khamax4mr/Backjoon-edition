# 숫자 a, b 입력.
a, b = map(int, input().split())
assert 0 < a < 10
assert 0 < b < 10

print(a * b)