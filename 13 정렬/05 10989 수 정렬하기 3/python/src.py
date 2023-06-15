from sys import exit, stdin, stdout

# 숫자 개수 n 입력.
n = int(stdin.readline().rstrip())
if n < 1 or n > 10000000: exit(0)

# 숫자 발생 횟수 기준으로 기록.
counts = [0] * 10001
for _ in range(n):
    number = int(stdin.readline().rstrip())
    if number <= 0 or number > 10000: exit(0)
    counts[number] += 1

for i in range(10001):
    for _ in range(counts[i]):
        stdout.write(str(i) + '\n')