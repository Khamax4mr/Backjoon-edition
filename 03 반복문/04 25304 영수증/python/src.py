# 총 금액 x 입력.
x = int(input())
assert 1 <= x <= 1000000000

# 구매 물건 종류 개수 n 입력.
n = int(input())
assert 1 <= n <= 100

# 영수증 총 금액 합산.
sum = 0
for _ in range(n):
    # 물건의 가격, 금액 a, b 입력.
    a, b = map(int, input().split())
    assert 1 <= a <= 1000000
    assert 1 <= b <= 10
    
    sum += a * b

print("Yes" if x == sum else "No")