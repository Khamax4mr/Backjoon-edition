# 입력 크기 n 입력.
n = int(input())
assert 1 <= n <= 500000

# MenOfPassion(A[], n) {
#   sum <- 0;
#   for i <- 1 to n
#       for j <- 1 to n
#           sum <- sum + A[i] × A[j]; # 코드1
#   return sum;
# }
print(n*n)
print(2)