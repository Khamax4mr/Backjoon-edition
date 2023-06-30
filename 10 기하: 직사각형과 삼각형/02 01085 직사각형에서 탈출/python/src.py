from sys import exit

# 가로 좌표 x, 세로 좌표 y, 너비 w, 높이 h 입력.
x, y, w, h = map(int, input().split())
if not 1 <= x <= w-1: exit()
if not 1 <= y <= h-1: exit()
if not 1 <= w <= 1000: exit()
if not 1 <= h <= 1000: exit()

print(min(x, w-x, y, h-y))