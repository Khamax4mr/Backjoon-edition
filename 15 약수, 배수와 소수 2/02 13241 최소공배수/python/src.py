# 숫자 a, b의 최소공배수를 구하는 함수.
# return 최소공배수
def lcm(a, b):
    # a를 큰 숫자로 가정.
    aa, bb = max(a, b), min(a, b)
    while aa % bb:
        aa, bb = bb, aa%bb
    return int(a * b / bb)

# 정수 a, b 입력.
a, b = map(int, input().split())
assert (a < 1000 and b < 1000) or (1000 < a < 10**8 and 1000 < b < 10**8)

print(lcm(a, b))