from sys import exit

# 정수 개수 n, 기준 정수 x 입력.
n, x = map(int, input().split())
if n < 1 or n > 10000: exit(0)
if x < 1 or x > 10000: exit(0)

# 배열 a 입력.
a = list(map(int, input().split()))
if True in [number < 1 or number > 10000 for number in a]: exit(0)

numbers_under_x = [elem for elem in a if elem < x]
print(' '.join(list(map(str, numbers_under_x))))