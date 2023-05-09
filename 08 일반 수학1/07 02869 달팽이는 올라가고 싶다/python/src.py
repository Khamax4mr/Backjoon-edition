from sys import exit
from math import ceil

# 올라가는 거리 a, 미끄러지는 거리 b, 높이 v 입력.
a, b, v = map(int, input().split())
if a < 1 or a > 1000000000: exit(0)
if b < 1 or b > 1000000000: exit(0)
if v < 1 or v > 1000000000: exit(0)

print(ceil((v-b) / (a-b)))