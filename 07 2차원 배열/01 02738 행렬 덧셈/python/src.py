from sys import exit

# 행 크기 n, 열 크기 m 입력.
n, m = map(int, input().split())
if n < 0 or n > 100: exit(0)
if m < 0 or m > 100: exit(0)

# 행렬 a, b 입력.
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
if True in [i < -100 or i > 100 for j in a for i in j ]: exit(0)
if True in [i < -100 or i > 100 for j in b for i in j ]: exit(0)

# 행렬 덧셈.
for i in range(n):
    row = [a[i][j] + b[i][j] for j in range(m)]
    print(' '.join(map(str, row)))