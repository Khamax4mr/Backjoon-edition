import sys
readline = sys.stdin.readline

# 집합 문자열 개수 n, 검사 문자열 개수 m 입력.
n, m = map(int, input().split())
assert 1 <= n <= 10000
assert 1 <= m <= 10000

# 집합 문자열 s 입력.
s = set(readline().rstrip() for _ in range(n))
assert not False in [len(word) > 500 for word in s]

# 검사 문자열 입력.
found = 0
for word in tuple(readline().rstrip() for _ in range(m)):
    assert len(word) <= 500
    assert word.islower()
    found += word in s

print(found)