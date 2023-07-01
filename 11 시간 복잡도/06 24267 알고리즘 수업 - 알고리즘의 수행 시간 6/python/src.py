from sys import exit

# 입력 크기 n 입력.
n = int(input())
if not 1 <= n <= 500000: exit()

# MenOfPassion(A[], n) {
#   sum <- 0;
#   for i <- 1 to n - 2
#       for j <- i + 1 to n - 1
#           for k <- j + 1 to n
#               sum <- sum + A[i] × A[j] × A[k]; # 코드1
#    return sum;
# }
print(int((n-2)*(n-1)*n / 6))
print(3)