# 색종이 개수 n 입력.
n = int(input())
assert 0 <= n <= 100

is_covered = [False] * 100 * 100
for _ in range(n):
    # 색종이-도화지 왼쪽 변 거리 x, 아래쪽 변 거리 y 입력.
    x, y = map(int, input().split())
    assert 0 <= x <= 90
    assert 0 <= y <= 90

    for i in range(10):
        is_covered[(y+i)*100 + x : (y+i)*100 + x+10] = [True] * 10

print(is_covered.count(True))