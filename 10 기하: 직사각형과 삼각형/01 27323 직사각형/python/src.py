from sys import exit

# 세로 길이 a, 가로 길이 b 입력.
a = int(input())
b = int(input())
if not 1 <= a <= 100: exit()
if not 1 <= b <= 100: exit()

print(a * b)