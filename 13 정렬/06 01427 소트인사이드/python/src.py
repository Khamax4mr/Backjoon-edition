from sys import exit

# 숫자 n 입력.
n = list(input())
if len(n) < 1 or len(n) > 10: exit(0)

n.sort(reverse=True)
print(''.join(map(str, n)))