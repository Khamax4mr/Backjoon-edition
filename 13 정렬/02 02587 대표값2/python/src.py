# 숫자들 numbers 입력.
numbers = [int(input()) for _ in range(5)]
assert not False in [number >= 100 or number % 10 for number in numbers]

numbers.sort()
print(int(sum(numbers) / 5))
print(numbers[2])