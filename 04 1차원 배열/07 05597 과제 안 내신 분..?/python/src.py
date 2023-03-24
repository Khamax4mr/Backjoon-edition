from sys import exit

# 제출 여부 초기화.
submit = [False for i in range(30)]

for i in range(28):
    # 제출 번호 n 입력.
    n = int(input())
    if n < 1 or n > 30: exit(0)

    # 0번부터 시작하는 번호 보정.
    correct_n = n - 1
    submit[correct_n] = True

# 출력.
for i in range(30):
    if submit[i] == True: continue
    print(i + 1)
