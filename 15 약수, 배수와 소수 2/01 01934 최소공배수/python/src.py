# 숫자 a, b의 최소공배수를 구하는 함수.
# return 최소공배수
def lcm(a, b):
    # a를 큰 숫자로 가정.
    aa, bb = max(a, b), min(a, b)
    while aa % bb:
        aa, bb = bb, aa%bb
    return int(a * b / bb)

# 테스트케이스 개수 t 입력.
t = int(input())
assert 1 <= t <= 1000

for _ in range(t):
    # 자연수 a, b 입력.
    a, b = map(int, input().split())
    assert 1 <= a <= 45000
    assert 1 <= b <= 45000

    print(lcm(a, b))