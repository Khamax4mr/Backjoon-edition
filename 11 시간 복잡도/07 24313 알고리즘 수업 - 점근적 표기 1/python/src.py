from sys import exit

# 함수 계수 a0, a1 입력.
a1, a0 = map(int, input().split())
if a0 < -100 or a0 > 100: exit(0)
if a1 < -100 or a1 > 100: exit(0)

# 상수 c 입력.
c = int(input())
if c < 1 or c > 100: exit(0)

# 최소값 n0 입력.
n0 = int(input())
if n0 < 1 or n0 > 100: exit(0)

print(1 if a1*n0 + a0 <= c*n0 and a1 <= c else 0)