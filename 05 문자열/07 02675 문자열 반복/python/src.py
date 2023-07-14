# 테스트 케이스 개수 t 입력.
t = int(input())
assert 1 <= t <= 1000

for _ in range(t):
    # 반복 횟수 r (정수형 repeats), 문자열 s 입력.
    r, s = map(str, input().split())
    repeats = int(r)
    assert 1 <= repeats <= 8
    assert 1 <= len(s) <= 20

    for j in range(len(s)):
        print(s[j] * repeats, end='')
    print()