# 숫자 n, 위치 k 입력.
n, k = map(int, input().split())
assert 1 <= n <= 10000
assert 1 <= k <= n

# 최소한의 반복으로 약수 판단 후 전체 약수 목록 구성.
base_divisors = [divisor for divisor in range(1, int(n**0.5)+1) if n % divisor == 0]
divisors = sorted(base_divisors + [n//divisor for divisor in base_divisors])
print(0 if len(divisors) < k else divisors[k-1])