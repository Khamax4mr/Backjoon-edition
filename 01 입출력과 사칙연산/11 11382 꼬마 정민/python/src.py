from sys import exit

# 숫자 a, b, c 입력.
a, b, c = map(int, input().split())
if a < 1 or a > 10**12: exit()
if b < 1 or b > 10**12: exit()
if c < 1 or c > 10**12: exit()

print(a + b + c)