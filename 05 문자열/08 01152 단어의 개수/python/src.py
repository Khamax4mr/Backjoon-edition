from sys import exit

# 문장 sentence 입력.
sentence = input()
if not 1 <= len(sentence) <= 1000000: exit()

print(len(sentence.split()))