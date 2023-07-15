import math
ceil = math.ceil

# 올라가는 거리 a, 미끄러지는 거리 b, 높이 v 입력.
a, b, v = map(int, input().split())
assert 1 <= a <= 1000000000
assert 1 <= b <= 1000000000
assert 1 <= v <= 1000000000

print(ceil((v-b) / (a-b)))