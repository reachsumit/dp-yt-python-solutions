# Problem: Climbing stairs
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can eitehr climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Objective Function:
# F(i) is the number of distinct ways to reach the i-th stair
#
# Recurrence relation:
# F(n) = F(n-1) + F(n-2)


def staircase(n):
    dp = []
    # Base cases: F(0) = 1, F(1) = 1
    dp.append(1)
    dp.append(1)

    # F(n) = F(n-1) + F(n-2)
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])

    return dp[n]


print(staircase(30))
