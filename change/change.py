def find_fewest_coins(coins, target):
    """
    Determine the fewest number of coins needed to make change for a target amount.
    
    Args:
        coins (list): List of integer values representing available coin denominations.
        target (int): The target amount for which to make change.
    
    Returns:
        list: A list of coin values that sum to the target amount, using the fewest
              possible coins. The returned list is sorted in ascending order.
    
    Raises:
        ValueError: If the target is negative, or if it's impossible to make the 
                   target amount with the available coins.
    
    Examples:
        >>> find_fewest_coins([1, 5, 10, 25], 15)
        [5, 10]
        >>> find_fewest_coins([1, 5, 10, 25, 100], 40)
        [5, 10, 25]
    """
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    if target > 0 and min(coins) > target:
        raise ValueError("can't make target with given coins")
    
    # Sort coins to optimize for some cases
    coins = sorted(coins)
    
    # Initialize dp arrays: dp[i] = minimum number of coins needed to make i
    # and coin_used[i] = the last coin used in the optimal solution for amount i
    dp = [float('inf')] * (target + 1)
    coin_used = [-1] * (target + 1)
    
    # Base case: 0 coins needed to make 0 change
    dp[0] = 0
    
    # Fill the dp table
    for i in range(1, target + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    # If no solution found
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")
    
    # Reconstruct the coin combination
    result = []
    remaining = target
    while remaining > 0:
        used_coin = coin_used[remaining]
        result.append(used_coin)
        remaining -= used_coin
    
    return sorted(result)
