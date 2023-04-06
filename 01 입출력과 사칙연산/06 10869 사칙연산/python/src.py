from sys import exit

# 숫자 a, b 입력.
a, b = map(int, input().split())
if a < 1 or a > 10000: exit(0)
if b < 1 or b > 10000: exit(0)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)