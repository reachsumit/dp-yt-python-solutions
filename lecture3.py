# Problem:
# find the sum of first n numbers
#
# Objective function:
# F(i) is the sum of first N numbers
#
# Recurrence relation:
# F(n) = F(n-1) + n


def nSum(n):
    dp = []
    # base case; F(0) = 0
    dp.append(0)

    # F(n) = F(n-1) + n
    for i in range(1, n+1):
        dp.append(dp[i-1] + i)

    return dp[n]


print(nSum(5))
