# 단어 word 입력.
word = input()
assert 1 <= len(word) <= 100
assert word.isalpha()

print(len(word))