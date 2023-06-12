from sys import exit

# 숫자들 numbers 입력.
numbers = [int(input()) for _ in range(5)]
if True in [number >= 100 or number % 10 for number in numbers]: exit(0)

numbers.sort()
print(int(sum(numbers) / 5))
print(numbers[2])