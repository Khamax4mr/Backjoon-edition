from sys import exit, stdin

# 테스트 케이스 개수 t 입력.
t = int(input())
if not 1 <= t <= 10: exit()

# 문자열 line 입력.
for line in stdin.readlines():
    string = line.rstrip()
    if not 1 <= len(string) <= 1000: exit()
    print(string[0] + string[-1])