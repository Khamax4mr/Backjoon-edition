from sys import exit

# 점 개수 n 입력.
n = int(input())
if n < 1 or n > 100000: exit(0)

# 점 좌표 marbles 입력.
marbles = [tuple(map(int, input().split())) for _ in range(n)]
marble_x = [marble[0] for marble in marbles]
marble_y = [marble[1] for marble in marbles]

min_x, max_x = min(marble_x), max(marble_x)
min_y, max_y = min(marble_y), max(marble_y)
if min_x < -10000 or max_x > 10000: exit(0)
if min_y < -10000 or max_y > 10000: exit(0)

print((max_x-min_x) * (max_y-min_y))