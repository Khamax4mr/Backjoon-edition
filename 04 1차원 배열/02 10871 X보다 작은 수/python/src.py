from sys import exit

# 정수 개수 n, 기준 정수 x 입력.
n, x = map(int, input().split())
if not 1 <= n <= 10000: exit()
if not 1 <= x <= 10000: exit()

# 배열 a 입력.
a = list(map(int, input().split()))
if True in [not 1 <= number <= 10000 for number in a]: exit()

numbers_under_x = [elem for elem in a if elem < x]
print(' '.join(list(map(str, numbers_under_x))))