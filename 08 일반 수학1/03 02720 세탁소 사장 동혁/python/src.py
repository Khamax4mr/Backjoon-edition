from sys import exit

# 테스트케이스 개수 t 입력.
t = int(input())

for _ in range(t):
    # 거스름돈 c 입력.
    c = int(input())
    if c < 1 or c > 500: exit(0)

    print(c // 25, (c%25) // 10, (c%25%10) // 5, c % 5)