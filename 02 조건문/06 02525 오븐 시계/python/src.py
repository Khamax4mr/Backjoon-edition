from sys import exit

# 시간 a, b, c 입력.
a, b = map(int, input().split())
c = int(input())
if a < 0 or a > 23: exit(0)
if b < 0 or b > 59: exit(0)
if c < 0 or c > 1000: exit(0)

# 시간 계산.
cooking_h, cooking_m = c//60, c%60
carry = (b + cooking_m) // 60
b = (b + cooking_m) % 60
a = (a + cooking_h + carry) % 24
print(a, b)