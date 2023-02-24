from sys import exit

# 숫자 a, b 입력.
a, b = map(int, input().split())
if a <= 0 or a >= 10: exit(0)
if b <= 0 or b >= 10: exit(0)

# 출력
print(a * b)