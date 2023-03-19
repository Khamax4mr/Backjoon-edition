from sys import exit

# 정수 개수 n 입력.
n = int(input())
if n < 1 or n > 1000000: exit(0)

# 배열 numbers 입력.
numbers = list(map(int, input().split()))
for elem in numbers:
    if elem < -1000000 or elem > 1000000: exit(0)

# 출력.
print(min(numbers), max(numbers))
