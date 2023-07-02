from sys import exit

# 영화 번호 n 입력.
n = int(input())
if not 0 < n <= 10000: exit()

numberings, i = [], 0
while len(numberings) <= n:
    # xxx666. (xx6666 제외)
    if i%10 != 6:
        numberings += [i*1000+666]
    # xx666x. (x6666x 제외)
    elif (i//10)%10 != 6:
        numberings += [i*1000+660+j for j in range(10)]
    # x666xx. (6666xx 제외)
    elif (i//10)%100 != 66:
        numberings += [i*1000+600+j for j in range(100)]
    # 666xxx.
    else:
        numberings += [i*1000+j for j in range(1000)]
    i += 1

print(numberings[n-1])