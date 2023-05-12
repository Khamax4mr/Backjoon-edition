from sys import exit

# 숫자 n, 위치 k 입력.
n, k = map(int, input().split())
if n < 1 or n > 10000: exit(0)
if k < 1 or k > n: exit(0)

divisors = []
for divisor in range(1, n+1):
    if n % divisor == 0: divisors.append(divisor)

print(0 if len(divisors) < k else divisors[k-1])