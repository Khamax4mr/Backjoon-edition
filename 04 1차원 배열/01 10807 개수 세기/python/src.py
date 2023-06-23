from sys import exit

# 정수 개수 n 입력.
n = int(input())
if not 1 <= n <= 100: exit()

# 정수 입력.
numbers = list(map(int, input().split()))
if True in [not -100 <= number <= 100 for number in numbers]: exit()

# 타겟 숫자 v 입력.
v = int(input())
if not -100 <= v <= 100: exit()

print(numbers.count(v))