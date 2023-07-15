# 점 개수 n 입력.
n = int(input())
assert 1 <= n <= 100000

marble_x, marble_y = [], []
for _ in range(n):
    # 점 좌표 x, y 입력.
    x, y = map(int, input().split())
    assert -10000 <= x <= 10000
    assert -10000 <= y <= 10000

    marble_x.append(x)
    marble_y.append(y)

print((max(marble_x)-min(marble_x)) * (max(marble_y)-min(marble_y)))