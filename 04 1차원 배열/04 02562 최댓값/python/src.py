from sys import exit

# 배열 numbers 입력.
numbers = [int(input()) for _ in range(9)]
if True in [not 1 <= number <= 100 for number in numbers]: exit()

print(max(numbers))
print(numbers.index(max(numbers)) + 1)