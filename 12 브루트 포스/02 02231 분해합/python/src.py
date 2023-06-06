from sys import exit

# 자연수 n 입력.
n = int(input())
if n < 1 or n > 1000000: exit(0)

constructors = []
for number in range(n):
    generated_number = number + sum(map(int, str(number)))
    # 분해합이 n이 아니면 넘어가기.
    if generated_number != n: continue
    constructors.append(number)

if len(constructors) > 0:
    print(min(constructors))
else:
    print(0)