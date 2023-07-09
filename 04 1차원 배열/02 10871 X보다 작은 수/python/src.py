from sys import exit

# 정수 개수 n, 기준 정수 x 입력.
n, x = map(int, input().split())
if not 1 <= n <= 10000: exit()
if not 1 <= x <= 10000: exit()

# 배열 입력.
numbers_under_x = []
for number in list(map(int, input().split())):
    if not 1 <= number <= 10000: exit()
    if number >= x: continue
    numbers_under_x.append(number)

print(' '.join(list(map(str, numbers_under_x))))