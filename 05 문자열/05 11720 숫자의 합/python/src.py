# 숫자 개수 n 입력.
n = int(input())
assert 1 <= n <= 100

# 공백 없는 숫자들 numbers 입력.
numbers = tuple(map(int, input()))
assert not False in [0 <= number <= 9 for number in numbers]

print(sum(numbers))