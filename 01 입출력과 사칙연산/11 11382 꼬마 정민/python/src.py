from sys import exit

# 숫자 a, b, c 입력.
inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

if a < 1 or a > 10**12: exit()
if b < 1 or b > 10**12: exit()
if c < 1 or c > 10**12: exit()

# 출력.
print(a + b + c)