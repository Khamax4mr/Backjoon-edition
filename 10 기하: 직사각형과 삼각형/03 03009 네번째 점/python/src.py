# 가로 좌표 목록 x_points, 세로 좌표 목록 y_points 입력.
x_points, y_points = [], []
for _ in range(3):
    x, y = map(int, input().split())
    assert 1 <= x <= 1000
    assert 1 <= y <= 1000

    x_points.append(x)
    y_points.append(y)

# 짝이 없는 좌표를 바탕으로 새로운 좌표 찾기.
x_points.sort()
y_points.sort()
print(x_points[2] if x_points[0] == x_points[1] else x_points[0],
      y_points[2] if y_points[0] == y_points[1] else y_points[0])