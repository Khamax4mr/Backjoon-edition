# 숫자 n이 소수인지 확인하는 함수.
# return n의 소수 여부.
def is_prime(n):
    if n == 0 or n == 1: return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0: return False
    return True

# 자연수 m, n 입력.
m, n = map(int, input().split())
assert 1 <= m <= 1000000
assert 1 <= n <= 1000000

for i in range(m, n+1):
    if not is_prime(i): continue
    print(i)