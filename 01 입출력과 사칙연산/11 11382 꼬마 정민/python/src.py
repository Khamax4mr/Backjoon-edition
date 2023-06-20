from sys import exit

# 숫자 a, b, c 입력.
a, b, c = map(int, input().split())
if not 1 <= a <= 10**12: exit()
if not 1 <= b <= 10**12: exit()
if not 1 <= c <= 10**12: exit()

print(a + b + c)