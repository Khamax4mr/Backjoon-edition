from sys import exit

# 아이디 문자 id 입력.
inputs = input().split()
id = inputs[0]

if len(id) > 50: exit()
if False in [a.islower() for a in id]: exit()

# 출력.
print(id + "??!")