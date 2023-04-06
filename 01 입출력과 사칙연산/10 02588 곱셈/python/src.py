from sys import exit

# 숫자 a, b 입력.
a = int(input())
b = int(input())
if a < 100 or a >= 1000: exit()
if b < 100 or b >= 1000: exit()

print(a * (b % 10))
print(a * (b % 100 // 10))
print(a * (b % 1000 // 100))
print(a * b)