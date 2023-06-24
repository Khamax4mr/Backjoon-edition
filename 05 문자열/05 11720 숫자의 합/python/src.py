from sys import exit

# 숫자 개수 n 입력.
n = int(input())
if not 1 <= n <= 100: exit()

# 공백 없는 숫자들 numbers 입력.
numbers = list(map(int, input()))
if True in [not 0 <= number <= 9 for number in numbers]: exit()
print(sum(numbers))