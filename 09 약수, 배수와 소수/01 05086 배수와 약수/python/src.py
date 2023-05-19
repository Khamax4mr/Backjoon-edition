from sys import exit

# 숫자 a, b의 최대공약수를 구하는 함수.
# return 최대공약수
def gcd(a, b):
    # a를 큰 숫자로 가정.
    a, b = max(a, b), min(a, b)
    while (a % b) and (b > 1):
        a = a % b
        a, b = max(a, b), min(a, b)
    return b

while True:
    # 숫자 a, b 입력.
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    if a < 0 or a > 10000: exit(0)
    if b < 0 or b > 10000: exit(0)

    if a % b == 0: print('multiple')
    elif gcd(a, b) > 1: print('factor')
    else: print('neither')