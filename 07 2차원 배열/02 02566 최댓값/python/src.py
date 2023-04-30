from sys import exit

matrix = []
for _ in range(9):
    # 숫자 한 줄 row 입력.
    row = list(map(int, input().split()))
    if True in [elem < 0 or elem > 100 for elem in row]: exit(0)
    matrix += row

max_number = max(matrix)
max_pos = matrix.index(max_number)
print(max_number)
print(max_pos // 9 + 1, max_pos % 9 + 1)