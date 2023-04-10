from sys import exit

# 단어 s 입력.
s = input()
if len(s) < 0 or len(s) > 100: exit(0)

# 알파벳 배치.
alphabets = [-1] * 26
for i in range(len(s)):
    # 알파벳 위치 등록.
    index = ord(s[i]) - ord('a')
    if alphabets[index] > -1: continue
    alphabets[index] = i

print(' '.join(list(map(str, alphabets))))