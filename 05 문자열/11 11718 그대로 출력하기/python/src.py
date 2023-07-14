import sys
readlines = sys.stdin.readlines

for line in readlines():
    sentence = line.rstrip()
    assert 0 <= len(sentence) <= 100
    print(sentence)