from sys import exit

# 테스트 케이스 개수 t 입력.
t = int(input())
if not 1 <= t <= 1000: exit()

for _ in range(t):
    # 반복 횟수 r (정수형 repeats), 문자열 s 입력.
    r, s = map(str, input().split())
    repeats = int(r)
    if not 1 <= repeats <= 8: exit()
    if not 1 <= len(s) <= 20: exit()

    for j in range(len(s)):
        print(s[j] * repeats, end='')
    print()