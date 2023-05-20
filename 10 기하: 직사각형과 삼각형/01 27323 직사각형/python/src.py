from sys import exit

# 세로 길이 a, 가로 길이 b 입력.
a = int(input())
b = int(input())
if a < 1 or a > 100: exit(0)
if b < 1 or b > 100: exit(0)

print(a * b)