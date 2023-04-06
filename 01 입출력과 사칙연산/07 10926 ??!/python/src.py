from sys import exit

# 아이디 문자 id 입력.
id = input()
if len(id) > 50: exit()
if False in [a.islower() for a in id]: exit()

print(id + "??!")