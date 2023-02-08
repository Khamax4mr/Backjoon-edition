from sys import exit

# 숫자 a, b 입력.
inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])

if a <= 0 or a >= 10: exit(0)
if b <= 0 or b >= 10: exit(0)

# 출력
print(a / b)