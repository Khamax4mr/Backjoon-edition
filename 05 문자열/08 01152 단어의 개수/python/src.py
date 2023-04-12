from sys import exit

# 문장 sentence 입력.
sentence = input()
if len(sentence) < 1 or len(sentence) > 1000000: exit(0)

print(len(sentence.split()))