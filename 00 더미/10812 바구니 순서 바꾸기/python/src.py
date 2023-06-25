from sys import exit

# 바구니 개수 n, 작업 횟수 m 입력.
n, m = map(int, input().split())
if n < 1 or n > 100: exit(0)
if m < 1 or m > 100: exit(0)

# 바구니 배치.
basket = [i for i in range(n+1)]
for process_iter in range(m):
    # 바구니 번호 i, j, k 입력.
    i, j, k = map(int, input().split())
    if i < 1 or i > n: exit(0)
    if j < 1 or j > n: exit(0)
    if k < 1 or k > n: exit(0)

    basket[i:j+1] = basket[k:j+1] + basket[i:k]

print(' '.join(list(map(str, basket[1:]))))