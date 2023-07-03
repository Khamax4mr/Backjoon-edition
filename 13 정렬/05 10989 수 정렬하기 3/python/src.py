from sys import exit, stdin, stdout

# 숫자 개수 n 입력.
n = int(input())
if not 1 <= n <= 10000000: exit()

# 숫자 발생 횟수 기준으로 기록.
counts = [0] * 10001
for _ in range(n):
    number = int(stdin.readline().rstrip())
    if not 0 < number <= 10000: exit()
    counts[number] += 1

for i in range(10001):
    for _ in range(counts[i]):
        stdout.write(str(i) + '\n')