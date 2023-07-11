from sys import exit, stdin

# 출입 기록 개수 n 입력.
n = int(input())
if not 2 <= n <= 100000: exit()

in_company = set()
for _ in range(n):
    # 이름 name, 출입 기록 action 입력.
    name, action = map(str, stdin.readline().rstrip().split())
    if len(name) > 5: exit()
    if not name.isalpha(): exit()
    if action not in ['enter', 'leave']: exit()

    if action == 'enter':
        in_company.add(name)
    else:
        in_company.remove(name)

print('\n'.join(sorted(in_company, reverse=True)))