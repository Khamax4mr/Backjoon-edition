from sys import exit, stdin

n = int(stdin.readline().rstrip())
if n < 1 or n > 1000000: exit(0)

numbers = [int(stdin.readline().rstrip()) for _ in range(n)]
if True in [number < -1000000 or number > 1000000 for number in numbers]: exit(0)

numbers.sort()
print('\n'.join(map(str, numbers)))