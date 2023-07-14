# 정수 개수 n 입력.
n = int(input())
assert 1 <= n <= 1000000

# 정수 목록 numbers 입력.
numbers = tuple(map(int, input().split()))
assert not False in [-1000000 <= number <= 1000000 for number in numbers]

print(min(numbers), max(numbers))