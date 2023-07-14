# 테스트 케이스 개수 t 입력.
t = int(input())
assert 1 <= t <= 10

# 문자열 line 입력.
for _ in range(t):
    string = input()
    assert 1 <= len(string) <= 1000
    assert string.isupper()
     
    print(string[0] + string[-1])