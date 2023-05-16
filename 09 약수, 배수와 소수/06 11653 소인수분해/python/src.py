from sys import exit

# 숫자 n 입력.
n = int(input())
if n < 1 or n > 10000000: exit(0)

# 정의에 따라 소인수분해가 불가능한 1은 생략.
if n == 1: pass

for divisor in range(2, n+1):
    while n % divisor == 0:
        print(divisor)
        n /= divisor