def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)

    dp[0] = 0

    for i in range(amount+1):
        for coin in coins:
            if i + coin <= amount:
                dp[i+coin] = min(dp[i+coin], dp[i] + 1)

    if dp[amount] == float("inf"):
        return -1

    return dp[amount]
