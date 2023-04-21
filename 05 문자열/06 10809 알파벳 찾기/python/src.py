from sys import exit

# 단어 s 입력.
s = input()
if len(s) < 0 or len(s) > 100: exit(0)

# 알파벳 배치.
alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
alphabet_index = [s.find(alphabet) for alphabet in alphabets]
print(' '.join(list(map(str, alphabet_index))))