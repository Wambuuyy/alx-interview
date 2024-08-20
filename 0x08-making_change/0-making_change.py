#!/usr/bin/python3
"""Given a pile of coins of different values,
determine the fewest no of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """return the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    # if total cant be met by any no of coins return -1
    # store the minimum coins for each amount from 0 to total
    # We use float('inf') as a placeholder for amounts that
    # cannot be reached with the given coins.
    dp = [float('inf')] * (total + 1)
    # Base case: To make the amount 0, we need 0 coins.
    dp[0] = 0
    # Iterate through each amount from 1 up to the total.
    for amount in range(1, total + 1):
        # Check each coin to see if it can be used to make the current amount.
        for coin in coins:
            # Only consider the coin if it is less than or equal to the current amount.
            if coin <= amount:
                # Update dp[amount] with the minimum coins needed:
                # Either the current value of dp[amount] or the value of dp[amount - coin] + 1
                # (i.e., using this coin).
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot be made with the given coins.
    return dp[total] if dp[total] != float('inf') else -1