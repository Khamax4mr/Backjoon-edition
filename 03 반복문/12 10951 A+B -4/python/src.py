from sys import stdin

for line in stdin.readlines():
    # 숫자 a, b 입력.
    a, b = map(int, line.rstrip().split())
    assert 0 < a < 10
    assert 0 < b < 10
    
    print(a + b)