from sys import exit

# 숫자 a, b 입력.
a, b = map(int, input().split())
if not 0 < a < 10: exit()
if not 0 < b < 10: exit()

print(a * b)