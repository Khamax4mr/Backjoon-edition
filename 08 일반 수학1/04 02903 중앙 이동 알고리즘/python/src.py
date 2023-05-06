from sys import exit

# 과정 반복 횟수 n 입력.
n = int(input())
if n < 1 or n > 15: exit(0)

row_dots = [2]
for i in range(n):
    row_dots.append(row_dots[i] + 2**i)

print(row_dots[n]**2)