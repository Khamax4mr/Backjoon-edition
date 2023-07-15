# 숫자 a, b 입력.
a, b = map(int, input().split())
assert a > 0 and len(str(a)) <= 10000
assert b > 0 and len(str(b)) <= 10000

print(a + b)