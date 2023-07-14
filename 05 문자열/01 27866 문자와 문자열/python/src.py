# 단어 s 입력.
s = input()
assert 1 <= len(s) <= 1000
assert s.isalpha()

# 위치 i 입력.
i = int(input())
assert 1 <= i <= len(s)

print(s[i-1])