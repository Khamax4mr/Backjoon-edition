# 이차원 배열 matrix 입력.
matrix = sum([list(map(int, input().split())) for _ in range(9)], [])
assert not False in [0 <= elem <= 100 for elem in matrix]

max_number = max(matrix)
max_pos = matrix.index(max_number)
print(max_number)
print(max_pos//9 + 1, max_pos%9 + 1)