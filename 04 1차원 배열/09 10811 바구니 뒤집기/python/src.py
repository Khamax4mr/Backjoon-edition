from sys import exit

# 바구니 개수 n, 작업 횟수 m 입력.
n, m = map(int, input().split())
if n < 1 or n > 100: exit(0)
if m < 1 or m > 100: exit(0)

# 바구니 번호 초기화.
basket = [i for i in range(1, n + 1)]

for process_iter in range(m):
    # 바구니 번호 i, j 입력.
    i, j = map(int, input().split())
    if i < 1 or i > n: exit(0)
    if j < 1 or j > n: exit(0)

    # 0번부터 시작하는 번호 보정.
    correct_i = i - 1
    correct_j = j - 1

    # 뒤집은 바구니 적용.
    reversed_basket = basket[correct_i : correct_j + 1]
    reversed_basket.reverse()
    basket[correct_i : correct_j + 1] = reversed_basket

# 출력.
print(' '.join(list(map(str, basket))))
