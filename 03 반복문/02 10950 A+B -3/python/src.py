from sys import exit

# 테스트케이스 개수 n 입력.
n = int(input())
if n < 0: exit(0)

for i in range(n):
    # 숫자 a, b 입력.
    a, b = map(int, input().split())
    if a <= 0 or a >= 10: exit(0)
    if b <= 0 or b >= 10: exit(0)
    
    print(a + b)