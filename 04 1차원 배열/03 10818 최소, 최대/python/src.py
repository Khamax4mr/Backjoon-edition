from sys import exit

n = int(input())
if not 1 <= n <= 1000000: exit()

numbers = list(map(int, input().split()))
if True in [not -1000000 <= number <= 1000000 for number in numbers]: exit()

print(min(numbers), max(numbers))