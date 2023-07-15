# 테스트케이스 개수 t 입력.
t = int(input())
assert t >= 0

for _ in range(t):
    # 거스름돈 c 입력.
    c = int(input())
    assert 1 <= c <= 500

    print(c // 25, (c%25) // 10, (c%25%10) // 5, c % 5)