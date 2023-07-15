import sys
readlines = sys.stdin.readlines

# 숫자 a, b의 최대공약수를 구하는 함수.
# return 최대공약수
def gcd(a, b):
    # a를 큰 숫자로 가정.
    a, b = max(a, b), min(a, b)
    while (a % b) and (b > 1):
        a = a % b
        a, b = max(a, b), min(a, b)
    return b

for line in readlines():
    # 숫자 a, b 입력.
    a, b = map(int, line.rstrip().split())
    if a == 0 and b == 0: break
    assert 0 <= a <= 10000
    assert 0 <= b <= 10000

    if a % b == 0: print('multiple')
    elif gcd(a, b) > 1: print('factor')
    else: print('neither')