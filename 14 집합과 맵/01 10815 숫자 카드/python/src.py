import sys
readline = sys.stdin.readline

# 보유 카드 개수 n 입력.
n = int(input())
assert 1 <= n <= 500000

# 보유 카드 숫자 hands 입력.
hands = set(map(int, readline().rstrip().split()))
assert not False in [-10000000 <= number <= 10000000 for number in hands]

# 비교 카드 개수 m 입력.
m = int(input())
assert 1 <= n <= 500000

# 비교 카드 숫자 matches 입력.
matches = tuple(map(int, readline().rstrip().split()))
assert not False in [-10000000 <= number <= 10000000 for number in matches]

print(' '.join(map(str, tuple(1 if number in hands else 0 for number in matches))))