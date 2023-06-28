from sys import exit

# 테스트케이스 개수 t 입력.
t = int(input())
if t < 0: exit()

for _ in range(t):
    # 거스름돈 c 입력.
    c = int(input())
    if not 1 <= c <= 500: exit()

    print(c // 25, (c%25) // 10, (c%25%10) // 5, c % 5)