from sys import exit

# 단어 word 입력.
word = input()
if len(word) < 1 or len(word) > 100: exit(0)

palindrome_state = False in [word[i] == word[-i-1] for i in range(len(word) // 2)]
print(0 if palindrome_state else 1)