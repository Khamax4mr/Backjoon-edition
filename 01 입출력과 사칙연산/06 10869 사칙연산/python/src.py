from sys import exit

# 숫자 a, b 입력.
inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])

if a < 1 or a > 10000: exit(0)
if b < 1 or b > 10000: exit(0)

# 출력
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)