from sys import exit

# 테스트케이스 개수 n 입력.
n = int(input())
if n < 0: exit()

for _ in range(n):
    # 숫자 a, b 입력.
    a, b = map(int, input().split())
    if not 0 < a < 10: exit()
    if not 0 < b < 10: exit()
    
    print(a + b)