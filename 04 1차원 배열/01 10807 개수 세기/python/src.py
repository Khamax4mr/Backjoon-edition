from sys import exit

# 정수 개수 n 입력.
n = int(input())
if n < 1 or n > 100: exit(0)

# 정수 입력.
numbers = list(map(int, input().split()))
if True in [number < -100 or number > 100 for number in numbers]: exit(0)

# 타겟 숫자 v 입력.
v = int(input())
if v < -100 or v > 100: exit(0)

print(numbers.count(v))