from sys import exit

# 과정 반복 횟수 n 입력.
n = int(input())
if not 1 <= n <= 15: exit()

row_dots = 2
for i in range(n):
    row_dots += 2**i
print(row_dots**2)