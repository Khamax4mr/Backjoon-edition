from sys import exit

# 숫자 a, b, c 입력.
inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

if a < 2 or a > 10000: exit()
if b < 2 or b > 10000: exit()
if c < 2 or c > 10000: exit()

# 출력.
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)