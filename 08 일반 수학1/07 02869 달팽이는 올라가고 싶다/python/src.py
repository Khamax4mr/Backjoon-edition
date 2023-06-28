from sys import exit
from math import ceil

# 올라가는 거리 a, 미끄러지는 거리 b, 높이 v 입력.
a, b, v = map(int, input().split())
if not 1 <= a <= 1000000000: exit()
if not 1 <= b <= 1000000000: exit()
if not 1 <= v <= 1000000000: exit()

print(ceil((v-b) / (a-b)))