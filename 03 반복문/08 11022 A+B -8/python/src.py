from sys import exit

# 테스트케이스 개수 t 입력.
t = int(input())
if t < 0: exit()

for i in range(t):
    # 숫자 a, b 입력.
    a, b = map(int, input().split())
    if not 0 < a < 10: exit()
    if not 0 < b < 10: exit()

    print(f"Case #{i+1}: {a} + {b} = {a + b}")