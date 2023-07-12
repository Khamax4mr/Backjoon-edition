from sys import exit, stdin

# 도감 수록 개수 n, 문제 개수 m 입력.
n, m = map(int, input().split())
if not 1 <= n <= 100000: exit()
if not 1 <= m <= 100000: exit()

poke_dict = {}
for i in range(1, n+1):
    # 포켓몬 이름 name 입력.
    name = stdin.readline().rstrip()
    if not 2 <= len(name) <= 20: exit()
    # 문제 오류 문의로 주석 처리.
    # if not ((name[0].isupper() and name[1:].islower()) ^ (name[-1].isupper() and name[:-1].islower())): exit()

    poke_dict[str(i)] = name
    poke_dict[name] = str(i)

for _ in range(m):
    # 문제 question 입력.
    question = stdin.readline().rstrip()

    # 유효한 문제는 응답.
    if question in poke_dict:
        print(poke_dict[question])
    else:
        exit()