from sys import exit

# 숫자 a, b 입력.
inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])

if a < -10000 or a > 10000: exit()
if b < -10000 or b > 10000: exit()

# 출력.
if a > b: print('>')
elif a < b: print('<')
else: print('==')