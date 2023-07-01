from sys import exit

# 함수 계수 a0, a1 입력.
a1, a0 = map(int, input().split())
if not -100 <= a0 <= 100: exit()
if not -100 <= a1 <= 100: exit()

# 상수 c 입력.
c = int(input())
if not 1 <= c <= 100: exit()

# 최소값 n0 입력.
n0 = int(input())
if not 1 <= n0 <= 100: exit()

print(1 if a1*n0 + a0 <= c*n0 and a1 <= c else 0)