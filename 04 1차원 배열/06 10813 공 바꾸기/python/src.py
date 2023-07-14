# 바구니 개수 n, 작업 횟수 m 입력.
n, m = map(int, input().split())
assert 1 <= n <= 100
assert 1 <= m <= 100

# 바구니 배치.
basket = [i for i in range(n+1)]
for _ in range(m):
    # 바구니 번호 i, j 입력.
    i, j = map(int, input().split())
    assert 1 <= i <= n
    assert 1 <= j <= n

    basket[i], basket[j] = basket[j], basket[i]

print(' '.join(map(str, basket[1:])))