from sys import exit

# 바구니 개수 n, 작업 횟수 m 입력.
n, m = map(int, input().split())
if n < 1 or n > 100: exit(0)
if m < 1 or m > 100: exit(0)

# 바구니 공 번호 초기화.
basket = [0 for i in range(n)]

for process_iter in range(m):
    # 시작 바구니 번호 i, 끝 바구니 번호 j, 공 번호 k 입력.
    i, j, k = map(int, input().split())
    if i < 1 or i > n: exit(0)
    if j < 1 or j > n: exit(0)
    if k < 1 or k > n: exit(0)

    # 바구니에 공 투입.
    for basket_iter in range(i - 1, j):
        basket[basket_iter] = k

# 출력.
print(' '.join(list(map(str, basket))))
