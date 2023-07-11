from sys import exit

# 글자 word 입력.
word = input()
if not word.isalnum(): exit()

print(ord(word))