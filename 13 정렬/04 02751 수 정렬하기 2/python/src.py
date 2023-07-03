from sys import exit, stdin

n = int(input())
if not 1 <= n <= 1000000: exit()

numbers = [int(stdin.readline().rstrip()) for _ in range(n)]
if True in [not -1000000 <= number <= 1000000 for number in numbers]: exit()

numbers.sort()
print('\n'.join(map(str, numbers)))