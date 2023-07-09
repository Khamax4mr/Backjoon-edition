from sys import exit, stdin

# 정수 개수 n 입력.
n = int(input())
if not 1 <= n <= 1000000: exit()

# 정수 목록 numbers 입력.
numbers = list(map(int, input().split()))
if True in [not -1000000 <= number <= 1000000 for number in numbers]: exit()

print(min(numbers), max(numbers))