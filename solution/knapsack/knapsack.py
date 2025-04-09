def maximum_value(maximum_weight, items):
    """
    Calculate the maximum value that can be carried in a knapsack with a weight limit.
    
    This function solves the 0/1 knapsack problem using dynamic programming. It finds the
    optimal selection of items that maximizes the total value while staying within the
    weight constraint. Each item can be selected at most once.
    
    Args:
        maximum_weight (int): The maximum weight the knapsack can hold.
        items (list): A list of dictionaries, where each dictionary represents an item
                     with 'weight' and 'value' keys.
                     
    Returns:
        int: The maximum possible value that can be carried in the knapsack.
        
    Example:
        >>> items = [
        ...     {"weight": 5, "value": 10},
        ...     {"weight": 4, "value": 40},
        ...     {"weight": 6, "value": 30},
        ...     {"weight": 4, "value": 50}
        ... ]
        >>> maximum_value(10, items)
        90
    """
    # Create a table to store the maximum value that can be obtained
    # for each weight limit from 0 to maximum_weight
    dp = [0] * (maximum_weight + 1)
    
    # For each item, consider whether to include it or not
    for item in items:
        weight, value = item["weight"], item["value"]
        
        # Update the table from right to left to avoid counting an item multiple times
        # (since we can take only one of each item)
        for w in range(maximum_weight, weight - 1, -1):
            # The maximum value at weight w is either:
            # 1. The current value at weight w (without taking this item)
            # 2. The value at (w - item's weight) plus this item's value (taking this item)
            dp[w] = max(dp[w], dp[w - weight] + value)
    
    # Return the maximum value possible with the given weight constraint
    return dp[maximum_weight]
