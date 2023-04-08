from sys import exit

# 총 금액 x 입력.
x = int(input())
if x < 1 or x > 1000000000: exit(0)

# 구매 물건 종류 개수 n 입력.
n = int(input())
if n < 1 or n > 100: exit(0)

# 영수증 총 금액 합산.
sum = 0
for i in range(n):
    # 물건의 가격, 금액 a, b 입력.
    a, b = map(int, input().split())
    if a < 1 or a > 1000000: exit(0)
    if b < 1 or b > 10: exit(0)
    
    sum += a * b

print("Yes" if x == sum else "No")