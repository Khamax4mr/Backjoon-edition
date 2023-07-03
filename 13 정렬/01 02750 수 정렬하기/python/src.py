from sys import exit

# 숫자 개수 n 입력.
n = int(input())
if not 1 <= n <= 1000: exit()

# 숫자들 numbers 입력.
numbers = [int(input()) for _ in range(n)]
if True in [not -1000 <= number <= 1000 for number in numbers]: exit()

numbers.sort()
print('\n'.join(map(str, numbers)))