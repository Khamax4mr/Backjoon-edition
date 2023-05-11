from sys import exit

while True:
    # 숫자 a, b 입력.
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    if a < 0 or a > 10000: exit(0)
    if b < 0 or b > 10000: exit(0)

    if a % b == 0: print('multiple')
    elif True in [not (a%i or b%i) for i in range(2, b//2)]: print('factor')
    else: print('neither')