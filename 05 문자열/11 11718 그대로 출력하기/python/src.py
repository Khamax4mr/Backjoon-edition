from sys import exit, stdin

for line in stdin.readlines():
    sentence = line.rstrip()
    if not 0 <= len(sentence) <= 100: exit()
    print(sentence)