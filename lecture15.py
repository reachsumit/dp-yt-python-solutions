def lecture15(coins, total):
    # [[cols] rows], i.e. total x len(coins)
    dp = [[0 for i in range(len(coins)+1)] for j in range(total+1)]

    for col in range(len(coins)+1):
        dp[0][col] = 1

    for i in range(total+1):
        for j in range(len(coins)):
            for k in range(j+1):
                if i-coins[k] >= 0:
                    dp[i][j] += dp[i-coins[k]][k]

    return dp[total][len(coins)-1]


def coinChange_unique(coins, total):
    # same as lecture 12
    dp = [0] * (total + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, total+1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]

    return dp[total]


print(lecture15([1, 2, 3, 5], 75))
print(coinChange_unique([1, 2, 3, 5], 75))
