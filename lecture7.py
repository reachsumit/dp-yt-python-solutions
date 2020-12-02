# Problem: Paid staircase
# You are climbing a paid staircas. It takes n steps to reach to the top and you have to
# pay p[i] to step on the i-th stair. Each time you can climb 1 or 2 steps.
# What's the cheapest amount you have to pay to get to the top of the staircase?
#
# Objective Function:
# F(i) is the minimum cost to get to the i-th stair
#
# Recurrence relation:
# F(n) = P(n) + min(F(n-1), F(n-2))


def paidStaircase(p, n):
    dp = []
    # Base cases: F(0) = 0 or P(0); F(1) = P(1)
    dp.append(0)
    dp.append(p[1])

    # F(n) = p[n] + min(F(n-1), F(n-2))
    for i in range(2, n+1):
        dp.append(p[i] + min(dp[i-1], dp[i-2]))

    return dp[n]


p = [0, 3, 2, 4]
print(paidStaircase(p, 3))
