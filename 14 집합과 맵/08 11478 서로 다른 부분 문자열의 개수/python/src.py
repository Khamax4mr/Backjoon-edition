# 문자열 s 입력.
s = input()
assert len(s) <= 1000

count = 0
for size in range(1, len(s)+1):
    partials = set(s[i:i+size] for i in range(len(s)-size+1))
    count += len(partials)
print(count)