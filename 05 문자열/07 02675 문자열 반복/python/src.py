from sys import exit

# 테스트 케이스 개수 t 입력.
t = int(input())
if t < 1 or t > 1000: exit(0)

for i in range(t):
    # 반복 횟수 r (정수형 repeats), 문자열 s 입력.
    r, s = input().split()
    repeats = int(r)
    if repeats < 1 or repeats > 8: exit(0)
    if len(s) < 1 or len(s) > 20: exit(0)

    for j in range(len(s)):
        print(s[j] * repeats, end='')
    print()