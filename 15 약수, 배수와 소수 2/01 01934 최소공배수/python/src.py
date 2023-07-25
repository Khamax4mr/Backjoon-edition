import math
lcm = math.lcm

# 테스트케이스 개수 t 입력.
t = int(input())
assert 1 <= t <= 1000

for _ in range(t):
    # 자연수 a, b 입력.
    a, b = map(int, input().split())
    assert 1 <= a <= 45000
    assert 1 <= b <= 45000

    print(lcm(a, b))