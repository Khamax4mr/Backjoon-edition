from sys import exit

# 테스트케이스 개수 t 입력.
t = int(input())

for _ in range(t):
    # 거스름돈 c 입력.
    c = int(input())
    if c < 1 or c > 500: exit(0)

    quarter = c // 25
    dime = (c % 25) // 10
    nickle = (c % 25 % 10) // 5
    penny = c % 5
    print(quarter, dime, nickle, penny)