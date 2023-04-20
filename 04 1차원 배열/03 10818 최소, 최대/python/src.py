from sys import exit

# 정수 개수 n 입력.
n = int(input())
if n < 1 or n > 1000000: exit(0)

# 배열 numbers 입력.
numbers = list(map(int, input().split()))
if True in [number < -1000000 or number > 1000000 for number in numbers]: exit(0)

print(min(numbers), max(numbers))