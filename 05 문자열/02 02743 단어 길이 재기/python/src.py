from sys import exit

# 단어 word 입력.
word = input()
if not 1 <= len(word) <= 100: exit()

print(len(word))