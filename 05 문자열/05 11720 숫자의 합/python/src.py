from sys import exit

# 숫자 개수 n 입력.
n = int(input())
if n < 1 or n > 100: exit(0)

# 공백 없는 숫자들 numbers 입력.
numbers = list(map(int, input()))
if True in [number < 0 or number > 9 for number in numbers]: exit(0)
print(sum(numbers))