from sys import exit

# 가로 좌표 x, 세로 좌표 y, 너비 w, 높이 h 입력.
x, y, w, h = map(int, input().split())
if x < 1 or x > w-1: exit(0)
if y < 1 or y > h-1: exit(0)
if w < 1 or w > 1000: exit(0)
if h < 1 or h > 1000: exit(0)

print(min(x, w-x, y, h-y))