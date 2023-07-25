import sys, math
readlines = sys.stdin.readlines
gcd = math.gcd

for line in readlines():
    # 숫자 a, b 입력.
    a, b = map(int, line.rstrip().split())
    if a == 0 and b == 0: break
    assert 0 <= a <= 10000
    assert 0 <= b <= 10000

    if a % b == 0: print('multiple')
    elif gcd(a, b) > 1: print('factor')
    else: print('neither')