from sys import exit

# 숫자 a, b 입력.
a, b = map(int, input().split())
if a <= 0 or len(str(a)) > 10000: exit()
if b <= 0 or len(str(b)) > 10000: exit()

print(a + b)