# 단어 word 입력.
word = input()
assert 1 <= len(word) <= 100
assert word.islower()

palindrome_state = False in [word[i] == word[-i-1] for i in range(len(word)//2)]
print(0 if palindrome_state else 1)