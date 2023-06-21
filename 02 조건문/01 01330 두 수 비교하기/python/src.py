from sys import exit

# 숫자 a, b 입력.
a, b = map(int, input().split())
if not -10000 <= a <= 10000: exit()
if not -10000 <= b <= 10000: exit()

if a > b: print('>')
elif a < b: print('<')
else: print('==')