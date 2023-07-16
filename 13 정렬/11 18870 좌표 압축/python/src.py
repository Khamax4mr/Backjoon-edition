import sys
readline = sys.stdin.readline

# 좌표 개수 n 입력.
n = int(input())
assert 1 <= n <= 1000000

# 좌표 points 입력.
points = list(map(int, readline().rstrip().split()))
assert not False in [not -10**9 <= x <= 10**9 for x in points]

points_set = sorted(set(points))
compressed_point_id = {points_set[i]:i for i in range(len(points_set))}
print(' '.join(map(str, tuple(compressed_point_id[x] for x in points))))