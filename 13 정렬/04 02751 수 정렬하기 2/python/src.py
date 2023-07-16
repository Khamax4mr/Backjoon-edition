import sys
readline = sys.stdin.readline

n = int(input())
assert 1 <= n <= 1000000

numbers = [int(readline().rstrip()) for _ in range(n)]
assert not False in [-1000000 <= number <= 1000000 for number in numbers]

numbers.sort()
print('\n'.join(map(str, numbers)))