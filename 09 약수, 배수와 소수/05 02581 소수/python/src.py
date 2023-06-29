from sys import exit

# 숫자 m, n 입력.
m = int(input())
n = int(input())
if not 0 <= m <= 10000: exit()
if not 0 <= n <= 10000: exit()

primes = []
for number in range(m, n+1):
    # 정의에 따라 소수가 아닌 1 생략.
    if number == 1: continue

    if True in [number % divisor == 0 for divisor in range(2, int(number**0.5)+1)]: continue
    primes.append(number)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])