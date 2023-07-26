# 숫자 n이 소수인지 확인하는 함수.
# return n의 소수 여부.
def is_prime(n):
    if n == 0 or n == 1: return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0: return False
    return True

# 테스트케이스 개수 testcases 입력.
testcases = int(input())
assert testcases > 0

for _ in range(testcases):
    # 정수 n 입력.
    n = int(input())
    assert 0 <= n <= 4 * 10**9

    while not is_prime(n): n += 1
    print(n)