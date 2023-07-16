# 입력 크기 n 입력.
n = int(input())
assert 1 <= n <= 500000

# MenOfPassion(A[], n) {
#   sum <- 0;
#   for i <- 1 to n - 1
#       for j <- i + 1 to n
#           sum <- sum + A[i] × A[j]; # 코드1
#   return sum;
# }
print(sum(range(n)))
print(2)