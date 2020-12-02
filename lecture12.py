def coinChange(coins, total):
    dp = [0] * (total + 1)
    dp[0] = 1

    for i in range(1, total+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] += dp[i-coin]

    return dp[total]


def coinChange_unique(coins, total):
    dp = [0] * (total + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, total+1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]

    return dp[total]


print(coinChange([1, 3, 5, 10], 4))
print(coinChange_unique([1, 3, 5, 10], 4))
