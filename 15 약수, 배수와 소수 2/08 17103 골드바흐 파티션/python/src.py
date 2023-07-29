# 테스트케이스 개수 t 입력.
t = int(input())
assert 1 <= t <= 100

is_prime = [False]*2 + [True]*(999999)
for i in range(2, int(1000000**0.5)+1):
    if not is_prime[i]: continue
    is_prime[i*2::i] = [False] * (1000000 // i - 1)

for _ in range(t):
    # 짝수 n 입력.
    n = int(input())
    assert n % 2 == 0
    assert 2 < n <= 1000000

    print([is_prime[i] and is_prime[n-i] for i in range(2, int(n/2)+1)].count(True))