from sys import exit

# 바구니 개수 n, 작업 횟수 m 입력.
n, m = map(int, input().split())
if not 1 <= n <= 100: exit()
if not 1 <= m <= 100: exit()

# 바구니 배치.
basket = [i for i in range(n+1)]
for _ in range(m):
    # 바구니 번호 i, j 입력.
    i, j = map(int, input().split())
    if not 1 <= i <= n: exit()
    if not 1 <= j <= n: exit()

    basket[i], basket[j] = basket[j], basket[i]

print(' '.join(list(map(str, basket[1:]))))