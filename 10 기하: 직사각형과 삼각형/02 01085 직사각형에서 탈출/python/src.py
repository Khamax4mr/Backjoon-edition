# 가로 좌표 x, 세로 좌표 y, 너비 w, 높이 h 입력.
x, y, w, h = map(int, input().split())
assert 1 <= x <= w-1
assert 1 <= y <= h-1
assert 1 <= w <= 1000
assert 1 <= h <= 1000

print(min(x, w-x, y, h-y))