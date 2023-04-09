from sys import exit

# 배열 numbers 입력.
numbers = [int(input()) for i in range(9)]
for elem in numbers:
    if elem < 1 or elem > 100: exit(0)

print(max(numbers))
print(numbers.index(max(numbers)) + 1)