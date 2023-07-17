import sys
readline = sys.stdin.readline
write = sys.stdout.write

# 보유 카드 개수 n 입력.
n = int(input())
assert 1 <= n <= 500000

# 보유 카드 번호 입력.
counts = {}
for number in map(str, readline().rstrip().split()):
    assert -10000000 <= int(number) <= 10000000

    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

# 검색 카드 개수 m 입력.
m = int(input())
assert 1 <= m <= 500000

# 검색 카드 번호 입력.
result = []
for number in map(str, readline().rstrip().split()):
    assert -10000000 <= int(number) <= 10000000
    result.append(counts[number] if number in counts else 0)
write(' '.join(map(str, result)))