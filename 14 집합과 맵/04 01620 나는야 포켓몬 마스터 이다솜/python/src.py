import sys
readline = sys.stdin.readline

# 도감 수록 개수 n, 문제 개수 m 입력.
n, m = map(int, input().split())
assert 1 <= n <= 100000
assert 1 <= m <= 100000

poke_dict = {}
for i in range(1, n+1):
    # 포켓몬 이름 name 입력.
    name = readline().rstrip()
    assert 2 <= len(name) <= 20
    assert name[0].isupper() and name[1:-1].islower() and name[-1].isalpha()

    poke_dict[str(i)] = name
    poke_dict[name] = str(i)

for _ in range(m):
    # 문제 question 입력.
    question = readline().rstrip()
    assert question in poke_dict

    print(poke_dict[question])