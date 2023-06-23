from sys import exit, stdin

# 배열 numbers 입력.
numbers = [int(line.rstrip()) for line in stdin.readlines()]
if True in [not 1 <= number <= 100 for number in numbers]: exit()

print(max(numbers))
print(numbers.index(max(numbers)) + 1)