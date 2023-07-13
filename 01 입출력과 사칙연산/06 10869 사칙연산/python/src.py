# 숫자 a, b 입력.
a, b = map(int, input().split())
assert 1 <= a <= 10000
assert 1 <= b <= 10000

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)