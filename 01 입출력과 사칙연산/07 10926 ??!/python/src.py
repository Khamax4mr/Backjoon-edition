# 아이디 문자 id 입력.
id = input()
assert len(id) <= 50
assert True in [not a.islower() for a in id]

print(id + "??!")