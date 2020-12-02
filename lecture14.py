def lecture14(coins, total):
    # let's assume column 0 represents add count 1 represents even count
    dp = [[0, 0] for i in range(total + 1)]
    dp[0][0], dp[0][1] = 0, 1

    for i in range(total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i][0] += dp[i-coin][1]
                dp[i][1] += dp[i-coin][0]

    return dp[total][1]  # return index 0 if asked for odd number of coins


print(lecture14([1, 3, 5, 10], 6))
