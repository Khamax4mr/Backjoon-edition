# 테스트케이스 개수 t 입력.
t = int(input())
assert t >= 0

for i in range(t):
    # 숫자 a, b 입력.
    a, b = map(int, input().split())
    assert 0 < a < 10
    assert 0 < b < 10

    print(f"Case #{i+1}: {a + b}")