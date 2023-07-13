# 테스트케이스 개수 n 입력.
n = int(input())
assert n >= 0

for _ in range(n):
    # 숫자 a, b 입력.
    a, b = map(int, input().split())
    assert 0 < a < 10
    assert 0 < b < 10
    
    print(a + b)