import sys
readline = sys.stdin.readline

# 회원 수 n 입력.
n = int(input())
assert 1 <= n <= 100000

members = []
for _ in range(n):
    # 나이 age, 이름 name 입력.
    age, name = readline().rstrip().split()
    age = int(age)
    assert 1 <= age <= 200
    assert len(name) <= 100

    members.append((age, name))

members.sort(key=lambda x : x[0])
print('\n'.join(' '.join(map(str, member)) for member in members))