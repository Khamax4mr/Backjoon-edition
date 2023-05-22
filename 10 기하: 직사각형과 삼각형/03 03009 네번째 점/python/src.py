from sys import exit

# 가로 좌표 목록 x_point, 세로 좌표 목록 y_point 입력.
x_point, y_point = [], []
for _ in range(3):
    x, y = map(int, input().split())
    if x < 1 or x > 1000: exit(0)
    if y < 1 or y > 1000: exit(0)

    x_point.append(x)
    y_point.append(y)

# 짝이 없는 좌표를 바탕으로 새로운 좌표 찾기.
new_x, new_y = 0, 0
for i in range(3):
    if x_point.count(x_point[i]) == 1:
        new_x = x_point[i] 
    if y_point.count(y_point[i]) == 1:
        new_y = y_point[i]

print(new_x, new_y)