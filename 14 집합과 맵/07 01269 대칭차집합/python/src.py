import sys
readline = sys.stdin.readline

# 집합 원소 개수 num_a, num_b 입력.
num_a, num_b = map(int, input().split())
assert 0 <= num_a <= 200000
assert 0 <= num_b <= 200000

# 집합 a 입력.
a = set(map(int, readline().rstrip().split()))
assert max(a) < 100000000

intersections = 0
# 집합 b 입력.
for elem in map(int, readline().rstrip().split()):
    assert elem < 100000000
    
    if elem not in a: continue
    intersections += 1

print(num_a + num_b - 2*intersections)