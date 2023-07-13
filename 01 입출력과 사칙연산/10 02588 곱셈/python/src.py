# 숫자 a, b 입력.
a = int(input())
b = int(input())
assert 100 <= a < 1000
assert 100 <= b < 1000

print(a * (b % 10))
print(a * (b % 100 // 10))
print(a * (b % 1000 // 100))
print(a * b)