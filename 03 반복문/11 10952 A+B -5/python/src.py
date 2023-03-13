from sys import exit

while True:
    # 숫자 a, b 입력.
    a, b = map(int, input().split())
    if a <= 0 or a >= 10: exit(0)
    if b <= 0 or b >= 10: exit(0)

    # 마지막 입력 확인.
    if not (a and b): break

    # 출력.
    print(a + b)
