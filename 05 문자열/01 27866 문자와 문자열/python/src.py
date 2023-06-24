from sys import exit

# 단어 s 입력.
s = input()
if not 1 <= len(s) <= 1000: exit()

# 위치 i 입력.
i = int(input())
if not 1 <= i <= len(s): exit()

print(s[i-1])