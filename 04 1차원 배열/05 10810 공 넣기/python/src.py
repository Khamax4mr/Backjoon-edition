from sys import exit

# 바구니 개수 n, 작업 횟수 m 입력.
n, m = map(int, input().split())
if not 1 <= n <= 100: exit()
if not 1 <= m <= 100: exit()

# 바구니 배치.
basket = [0] * (n+1)
for _ in range(m):
    # 시작 바구니 번호 i, 끝 바구니 번호 j, 공 번호 k 입력.
    i, j, k = map(int, input().split())
    if not 1 <= i <= n: exit()
    if not 1 <= j <= n: exit()
    if not 1 <= k <= n: exit()

    basket[i : j+1] = [k] * (j - i + 1)

print(' '.join(list(map(str, basket[1:]))))