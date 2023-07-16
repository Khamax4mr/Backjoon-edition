import sys
readline = sys.stdin.readline
write = sys.stdout.write

# 숫자 개수 n 입력.
n = int(input())
assert 1 <= n <= 10000000

# 숫자 발생 횟수 기준으로 기록.
counts = [0] * 10001
for _ in range(n):
    number = int(readline().rstrip())
    assert 0 < number <= 10000
    counts[number] += 1

for i in range(10001):
    for _ in range(counts[i]):
        write(str(i) + '\n')