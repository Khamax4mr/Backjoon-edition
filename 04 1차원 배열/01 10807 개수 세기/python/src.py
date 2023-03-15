from sys import exit

# 정수 개수 n 입력.
n = int(input())
if n < 1 or n > 100: exit(0)

# 정수 입력.
numbers = list(map(int, input().split()))
for elem in numbers:
    if elem < -100 or elem > 100: exit(0)

# 타겟 숫자 v 입력.
v = int(input())
if v < -100 or v > 100: exit(0)

# 출력.
print(numbers.count(v))
