# 함수 계수 a0, a1 입력.
a1, a0 = map(int, input().split())
assert -100 <= a0 <= 100
assert -100 <= a1 <= 100

# 상수 c 입력.
c = int(input())
assert 1 <= c <= 100

# 최소값 n0 입력.
n0 = int(input())
assert 1 <= n0 <= 100

print(1 if a1*n0 + a0 <= c*n0 and a1 <= c else 0)