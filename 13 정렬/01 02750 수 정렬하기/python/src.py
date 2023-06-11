from sys import exit

# 숫자 개수 n 입력.
n = int(input())
if n < 1 or n > 1000: exit(0)

# 숫자들 numbers 입력.
numbers = [int(input()) for _ in range(n)]
if True in [number < -1000 or number > 1000 for number in numbers]: exit(0)

numbers.sort()
print('\n'.join(map(str, numbers)))