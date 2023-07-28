import sys
readlines = sys.stdin.readlines

# 소수 목록 생성.
max_n = 123456 * 2
is_prime = [False]*2 + [True]*(max_n-1)
for i in range(2, int(max_n**0.5)+1):
    if not is_prime[i]: continue
    is_prime[i*2::i] = [False] * (max_n // i - 1)

for line in readlines():
    # 자연수 n 입력.
    n = int(line.rstrip())
    if n == 0: break
    assert 1 <= n <= 123456

    print(is_prime[n+1:2*n+1].count(True))