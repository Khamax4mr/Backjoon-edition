from sys import exit

# 배열 numbers 입력.
numbers = [int(input()) for i in range(9)]
if True in [number < 1 or number > 100 for number in numbers]: exit(0)

print(max(numbers))
print(numbers.index(max(numbers)) + 1)