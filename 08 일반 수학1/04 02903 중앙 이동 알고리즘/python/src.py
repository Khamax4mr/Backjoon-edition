# 과정 반복 횟수 n 입력.
n = int(input())
assert 1 <= n <= 15

row_dots = 2
for i in range(n):
    row_dots += 2**i
print(row_dots**2)