# 숫자 개수 n 입력.
n = int(input())
assert 1 <= n <= 1000

# 숫자들 numbers 입력.
numbers = [int(input()) for _ in range(n)]
assert not False in [not -1000 <= number <= 1000 for number in numbers]

numbers.sort()
print('\n'.join(map(str, numbers)))