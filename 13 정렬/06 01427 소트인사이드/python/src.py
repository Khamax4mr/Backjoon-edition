from sys import exit

# 숫자 n 입력.
n = list(input())
if not 1 <= len(n) <= 10: exit()

n.sort(reverse=True)
print(''.join(map(str, n)))