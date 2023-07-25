import sys, math
readlines = sys.stdin.readlines
gcd = math.gcd

# 가로수 개수 n 입력.
n = int(input())
assert 3 <= n <= 100000

# 가로수 위치 positions 입력.
positions = tuple(int(line.rstrip()) for line in readlines())
assert not False in [0 < position <= 1000000000 for position in positions]

distances = [j-i for i,j in zip(positions[:-1], positions[1:])]
overall_gcd = gcd(*distances)
print(int((sum(distances) - overall_gcd * len(distances)) / overall_gcd))