# 배열 numbers 입력.
numbers = tuple(int(input()) for _ in range(9))
assert not False in [1 <= number <= 100 for number in numbers]

print(max(numbers))
print(numbers.index(max(numbers)) + 1)