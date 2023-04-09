from sys import exit

# 제출 여부 구성.
submit = [False] * 31
for i in range(28):
    # 제출 번호 n 입력.
    n = int(input())
    if n < 1 or n > 30: exit(0)
    
    submit[n] = True

# 미제출 번호 출력.
for i in range(1, 31):
    if submit[i] == True: continue
    print(i)