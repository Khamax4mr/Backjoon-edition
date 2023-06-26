from sys import exit

# 색종이 개수 n 입력.
n = int(input())
if not 0 <= n <= 100: exit()

is_covered = [False] * 100 * 100
for _ in range(n):
    # 색종이-도화지 왼쪽 변 거리 x, 아래쪽 변 거리 y 입력.
    x, y = map(int, input().split())
    if not 0 <= x <= 90: exit()
    if not 0 <= y <= 90: exit()

    for i in range(10):
        is_covered[(y+i)*100 + x : (y+i)*100 + x+10] = [True] * 10

print(is_covered.count(True))