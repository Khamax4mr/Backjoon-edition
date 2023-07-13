# 숫자 a, b 입력.
a, b = map(int, input().split())
assert -10000 <= a <= 10000
assert -10000 <= b <= 10000

if a > b: print('>')
elif a < b: print('<')
else: print('==')