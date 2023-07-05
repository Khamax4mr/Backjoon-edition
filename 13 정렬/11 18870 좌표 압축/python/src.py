from sys import exit, stdin

# 좌표 개수 n 입력.
n = int(input())
if not 1 <= n <= 1000000: exit()

# 좌표 points 입력.
points = list(map(int, stdin.readline().rstrip().split()))
if True in [not -10**9 <= x <= 10**9 for x in points]: exit()

points_set = list(set(points))
points_set.sort()
compressed_point_id = {points_set[i]:i for i in range(len(points_set))}
compressed_points = [compressed_point_id[x] for x in points]
print(' '.join(map(str, compressed_points)))