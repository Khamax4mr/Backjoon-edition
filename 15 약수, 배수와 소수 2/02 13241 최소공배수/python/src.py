import math
lcm = math.lcm

# 정수 a, b 입력.
a, b = map(int, input().split())
assert (a < 1000 and b < 1000) or (1000 < a < 10**8 and 1000 < b < 10**8)

print(lcm(a, b))