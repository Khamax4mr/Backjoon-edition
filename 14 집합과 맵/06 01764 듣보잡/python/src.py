import sys
readline = sys.stdin.readline

# 듣도 못한 사람 수 n, 보도 못한 사람 수 m 입력.
n, m = map(int, input().split())
assert 1 <= n <= 500000
assert 1 <= m <= 500000

names = []
for _ in range(n+m):
    # 사람 이름 name 입력.
    name = readline().rstrip()
    assert len(name) <= 20

    names.append(name)

unheards = set(names[:n])
unseens = set(names[n:])
unknowns = sorted(unheards & unseens)
print(len(unknowns))
print('\n'.join(unknowns))