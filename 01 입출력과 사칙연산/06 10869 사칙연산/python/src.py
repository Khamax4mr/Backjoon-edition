from sys import exit

# 숫자 a, b 입력.
a, b = map(int, input().split())
if not 1 <= a <= 10000: exit()
if not 1 <= b <= 10000: exit()

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)