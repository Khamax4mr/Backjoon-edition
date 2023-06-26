from sys import exit, stdin

matrix = sum([list(map(int, line.rstrip().split())) for line in stdin.readlines()], [])
if True in [not 0 <= elem <= 100 for elem in matrix]: exit()

max_number = max(matrix)
max_pos = matrix.index(max_number)
print(max_number)
print(max_pos//9 + 1, max_pos%9 + 1)