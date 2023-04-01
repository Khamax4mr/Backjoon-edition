from sys import exit

# 테스트 케이스 개수 t 입력.
t = int(input())
if t < 1 or t > 10: exit(0)

for i in range(t):
    # 문자열 string 입력.
    string = input()
    if len(string) < 1 or len(string) > 1000: exit(0)

    # 출력.
    print(string[0] + string[-1])
