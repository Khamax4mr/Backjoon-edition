from sys import exit
from math import sqrt

# 숫자 m, n 입력.
m = int(input())
n = int(input())
if m < 0 or m > 10000: exit(0)
if n < 0 or n > 10000: exit(0)

primes = []
for number in range(m, n+1):
    # 정의에 따라 소수가 아닌 1 생략.
    if number == 1: continue

    is_dividable = [number % divisor == 0 for divisor in range(2, int(sqrt(number))+1)]
    if True in is_dividable: continue
    primes.append(number)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])