import string
alphabets = string.ascii_lowercase

# 단어 s 입력.
s = input()
assert 0 <= len(s) <= 100
assert s.islower()

alphabet_index = tuple(s.find(alphabet) for alphabet in alphabets)
print(' '.join(map(str, alphabet_index)))