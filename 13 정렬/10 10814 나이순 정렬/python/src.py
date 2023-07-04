from sys import exit, stdin

# 회원 수 n 입력.
n = int(input())
if not 1 <= n <= 100000: exit()

members = []
for _ in range(n):
    # 나이 age, 이름 name 입력.
    age, name = stdin.readline().rstrip().split()
    age = int(age)
    if not 1 <= age <= 200: exit()
    if len(name) > 100: exit()

    members.append((age, name))

members.sort(key=lambda x : x[0])
print('\n'.join([' '.join(map(str, member)) for member in members]))