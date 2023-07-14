# 바구니 개수 n, 작업 횟수 m 입력.
n, m = map(int, input().split())
assert 1 <= n <= 100
assert 1 <= m <= 100

# 바구니 배치.
basket = [0] * (n+1)
for _ in range(m):
    # 시작 바구니 번호 i, 끝 바구니 번호 j, 공 번호 k 입력.
    i, j, k = map(int, input().split())
    assert 1 <= i <= n
    assert 1 <= j <= n
    assert 1 <= k <= n

    basket[i : j+1] = [k] * (j - i + 1)

print(' '.join(map(str, basket[1:])))