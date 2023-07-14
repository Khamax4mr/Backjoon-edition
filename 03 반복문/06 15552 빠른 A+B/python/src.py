import sys
readline = sys.stdin.readline
write = sys.stdout.write

# 테스트케이스 개수 t 입력.
t = int(readline().rstrip())
assert 0 < t <= 1000000

sum = []
for _ in range(t):
    # 숫자 a, b 입력.
    a, b = map(int, readline().rstrip().split())
    assert 1 <= a <= 1000
    assert 1 <= b <= 1000

    sum.append(a + b)

write('\n'.join(map(str, sum)))