from sys import exit

# 숫자 m, n 입력.
m = int(input())
n = int(input())
if m < 0 or m > 10000: exit(0)
if n < 0 or n > 10000: exit(0)

no_divisors = []
for number in range(m, n+1):
    # 정의에 따라 소수가 아닌 1 생략.
    if number == 1: continue

    is_dividable = [number % divisor == 0 for divisor in range(2, number//2+1)]
    if True in is_dividable: continue
    no_divisors.append(number)

if len(no_divisors) == 0:
    print(-1)
else:
    print(sum(no_divisors))
    print(no_divisors[0])