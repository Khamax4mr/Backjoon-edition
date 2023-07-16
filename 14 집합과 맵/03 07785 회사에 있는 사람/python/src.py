import sys
readline = sys.stdin.readline

# 출입 기록 개수 n 입력.
n = int(input())
assert 2 <= n <= 100000

in_company = set()
for _ in range(n):
    # 이름 name, 출입 기록 action 입력.
    name, action = map(str, readline().rstrip().split())
    assert len(name) <= 5
    assert name.isalpha()
    assert action in ('enter', 'leave')

    if action == 'enter':
        in_company.add(name)
    else:
        in_company.remove(name)

print('\n'.join(sorted(in_company, reverse=True)))