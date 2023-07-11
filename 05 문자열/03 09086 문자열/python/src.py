from sys import exit

# 테스트 케이스 개수 t 입력.
t = int(input())
if not 1 <= t <= 10: exit()

# 문자열 line 입력.
for _ in range(t):
    string = input()
    if not 1 <= len(string) <= 1000: exit()
    if not string.isupper(): exit()
  
    print(string[0] + string[-1])