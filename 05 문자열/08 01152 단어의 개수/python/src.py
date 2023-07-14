# 문장 sentence 입력.
sentence = input()
assert 1 <= len(sentence) <= 1000000
assert not False in [s.isalpha() for s in sentence.split()]

print(len(sentence.split()))