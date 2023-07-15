# 행 크기 n, 열 크기 m 입력.
n, m = map(int, input().split())
assert 0 <= n <= 100
assert 0 <= m <= 100

# 행렬 a, b 입력.
a = tuple(tuple(map(int, input().split())) for _ in range(n))
b = tuple(tuple(map(int, input().split())) for _ in range(n))
assert not False in [-100 <= i <= 100 for j in a for i in j]
assert not False in [-100 <= i <= 100 for j in b for i in j]

# 행렬 덧셈.
for i in range(n):
    row = tuple(a[i][j] + b[i][j] for j in range(m))
    print(' '.join(map(str, row)))