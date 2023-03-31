from sys import exit

# 단어 word 입력.
word = input()
if len(word) < 1 or len(word) > 100: exit(0)

# 출력.
print(len(word))
