from sys import exit

# 단어 s 입력.
s = input()
if len(s) < 1 or len(s) > 1000: exit(0)

# 위치 i 입력.
i = int(input())
if i < 1 or i > len(s): exit(0)

# 0번부터 시작하는 번호 보정.
correct_i = i - 1

# 출력.
print(s[correct_i])
