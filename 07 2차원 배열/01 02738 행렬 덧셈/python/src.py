from sys import exit

# 행 크기 n, 열 크기 m 입력.
n, m = map(int, input().split())
if not 0 <= n <= 100: exit()
if not 0 <= m <= 100: exit()

# 행렬 a, b 입력.
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
if True in [not -100 <= i <= 100 for j in a for i in j ]: exit()
if True in [not -100 <= i <= 100 for j in b for i in j ]: exit()

# 행렬 덧셈.
for i in range(n):
    row = [a[i][j] + b[i][j] for j in range(m)]
    print(' '.join(map(str, row)))