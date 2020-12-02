def lecture17(coins, total):
    dp = [float('inf')] * (total+1)
    dp[0] = 0

    for i in range(1, total+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[total] if dp[total] != float('inf') else "No Answer"


print(lecture17([1, 3, 5], 29))
