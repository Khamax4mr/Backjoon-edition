from sys import exit

# 숫자 개수 n 입력.
n = int(input())
if n < 0 or n > 100: exit(0)

# 숫자 numbers 입력.
numbers = list(map(int, input().split()))
if True in [number < 0 or number > 1000 for number in numbers]: exit(0)

no_divisor_count = 0
for number in numbers:
    # 정의에 따라 소수가 아닌 1 생략.
    if number == 1: continue

    is_dividable = [number % divisor == 0 for divisor in range(2, number//2+1)] 
    no_divisor_count += True not in is_dividable

print(no_divisor_count)