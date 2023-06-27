from sys import exit

matrix = sum([list(map(int, input().split())) for _ in range(9)], [])
if True in [not 0 <= elem <= 100 for elem in matrix]: exit()

max_number = max(matrix)
max_pos = matrix.index(max_number)
print(max_number)
print(max_pos//9 + 1, max_pos%9 + 1)