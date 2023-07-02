from sys import exit

# 자연수 n 입력.
n = int(input())
if not 1 <= n <= 1000000: exit()

constructors = []
for number in range(n-1, 0, -1):
    generated_number = number + sum(map(int, str(number)))
    # 더이상 n에 도달할 수 없으면 중단.
    if generated_number < n - (len(str(number))-1)*10: break
    # 분해합이 n이 아니면 넘어가기.
    if generated_number != n: continue
    constructors.append(number)

if len(constructors) > 0:
    print(min(constructors))
else:
    print(0)