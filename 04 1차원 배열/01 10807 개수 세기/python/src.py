# 정수 개수 n 입력.
n = int(input())
assert 1 <= n <= 100

# 정수 입력.
numbers = tuple(map(int, input().split()))
assert not False in [-100 <= number <= 100 for number in numbers]

# 타겟 숫자 v 입력.
v = int(input())
assert -100 <= v <= 100

print(numbers.count(v))