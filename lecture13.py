def lecture13_exactly_t(coins, required_sum, max_coins_count):
    # required_sum is n and max_coins_count is t
    dp = [[0 for i in range(max_coins_count + 1)]
          for j in range(required_sum + 1)]  # [[cols] rows] i.e. n x t
    dp[0][0] = 1

    for i in range(required_sum + 1):
        for j in range(max_coins_count + 1):
            if i > 0 and j == 0:
                continue
            for coin in coins:
                if i - coin >= 0:
                    dp[i][j] += dp[i - coin][j - 1]

    return dp[required_sum][max_coins_count]


def lecture13_no_more_than_t(coins, required_sum, max_coins_count):
    # required_sum is n and max_coins_count is t
    dp = [[0 for i in range(max_coins_count + 1)]
          for j in range(required_sum + 1)]  # [[cols] rows] i.e. n x t
    dp[0][0] = 1

    for i in range(required_sum + 1):
        for j in range(max_coins_count + 1):
            if i > 0 and j == 0:
                continue
            if i == 0 and j > 0:
                dp[i][j] = 1
                continue

            for coin in coins:
                if i - coin >= 0:
                    dp[i][j] += dp[i-coin][j-1]

    return dp[required_sum][max_coins_count]


print(lecture13_exactly_t([1, 2, 3, 5], 7, 3))
print(lecture13_no_more_than_t([1, 2, 3, 5], 7, 3))
