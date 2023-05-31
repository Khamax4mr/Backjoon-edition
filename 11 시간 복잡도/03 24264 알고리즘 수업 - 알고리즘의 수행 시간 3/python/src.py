from sys import exit

# 입력 크기 n 입력.
n = int(input())
if n < 1 or n > 500000: exit(0)

# MenOfPassion(A[], n) {
#   sum <- 0;
#   for i <- 1 to n
#       for j <- 1 to n
#           sum <- sum + A[i] × A[j]; # 코드1
#   return sum;
# }
print(n*n)
print(2)