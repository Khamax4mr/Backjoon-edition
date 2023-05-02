from sys import exit

# 색종이 개수 n 입력.
n = int(input())
if n < 0 or n > 100: exit(0)

is_covered = [False for _ in range(100 * 100)]
for _ in range(n):
    # 색종이-도화지 왼쪽 변 거리 x, 아래쪽 변 거리 y 입력.
    x, y = map(int, input().split())
    if x < 0 or x > 90: exit(0)
    if y < 0 or y > 90: exit(0)

    for i in range(10):
        is_covered[(y+i)*100 + x : (y+i)*100 + x+10] = [True] * 10

print(is_covered.count(True))