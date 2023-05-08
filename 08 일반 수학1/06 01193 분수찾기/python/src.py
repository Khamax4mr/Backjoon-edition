from sys import exit

# 위치 x 입력.
x = int(input())
if x < 1 or x > 10000000: exit(0)

# 배열의 줄 row, 최대 번호 max_id_in_row.
row, max_id_in_row = 1, 0
while max_id_in_row < x:
    max_id_in_row += row
    row += 1

if row % 2 == 0:
    print(f"{max_id_in_row - x + 1}/{row - max_id_in_row + x - 1}")
else:
    print(f"{row - max_id_in_row + x - 1}/{max_id_in_row - x + 1}")