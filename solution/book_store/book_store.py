def total(basket):
    """
    Calculate the total price for a basket of books, applying optimal discounts.
    
    The bookstore offers discounts for buying multiple different books:
    - No discount for a single book
    - 5% discount for 2 different books
    - 10% discount for 3 different books
    - 20% discount for 4 different books
    - 25% discount for all 5 different books
    
    This function finds the optimal way to group books to maximize discounts.
    
    Args:
        basket (list): A list of book identifiers (1-5)
    
    Returns:
        int: The total price in cents after applying optimal discounts
    """
    if not basket:
        return 0
    
    # Count the occurrences of each book
    book_counts = {}
    for book in basket:
        book_counts[book] = book_counts.get(book, 0) + 1
    
    # Define the discount rates for different group sizes
    discounts = {
        1: 0,      # no discount for one book
        2: 0.05,   # 5% discount for two different books
        3: 0.10,   # 10% discount for three different books
        4: 0.20,   # 20% discount for four different books
        5: 0.25    # 25% discount for five different books
    }
    
    # The base price for one book
    BASE_PRICE = 800
    
    # The key insight is that groups of 4 books (with 20% discount)
    # are often better than certain combinations like 5+3 (25% + 10% discount)
    # We need to find the optimal grouping
    
    def calculate_price(groups):
        """
        Calculate price for a specific grouping of books.
        
        Args:
            groups (dict): Dictionary with group sizes as keys and counts as values
        
        Returns:
            float: Total price for the given grouping
        """
        price = 0
        for group_size, count in groups.items():
            price += group_size * BASE_PRICE * (1 - discounts[group_size]) * count
        return price
    
    # Try different grouping strategies
    def optimize_grouping():
        """
        Find the optimal grouping of books to minimize the total price.
        
        The function first uses a greedy approach to form the largest possible groups,
        then tries optimizations like converting groups of 5+3 books into 4+4 books
        when that would result in a better total discount.
        
        Returns:
            int: The optimized total price in cents
        """
        # Initialize with a greedy approach (always take largest possible groups)
        remaining = book_counts.copy()
        groups = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        
        # Form groups until no books remain
        while sum(remaining.values()) > 0:
            # Find number of available unique books
            unique_books = [b for b, count in remaining.items() if count > 0]
            group_size = len(unique_books)
            
            # Take one of each available book
            for book in unique_books:
                remaining[book] -= 1
                if remaining[book] == 0:
                    del remaining[book]
            
            # Increment the group count
            groups[group_size] += 1
        
        base_price = calculate_price(groups)
        
        # Try optimizations by converting groups of 5 + 3 to 4 + 4
        optimized_price = base_price
        optimized_groups = groups.copy()
        
        # While we have at least one group of 5 and one group of 3
        temp_groups = groups.copy()
        while temp_groups.get(5, 0) > 0 and temp_groups.get(3, 0) > 0:
            # Convert one group of 5 and one group of 3 into two groups of 4
            temp_groups[5] -= 1
            temp_groups[3] -= 1
            temp_groups[4] = temp_groups.get(4, 0) + 2
            
            # Calculate the new price
            new_price = calculate_price(temp_groups)
            
            # If better, update our optimized price
            if new_price < optimized_price:
                optimized_price = new_price
                optimized_groups = temp_groups.copy()
            else:
                # If not improving, stop trying
                break
        
        return int(optimized_price)
    
    # Special case: equal copies of all 5 books
    if len(book_counts) == 5 and all(count == list(book_counts.values())[0] for count in book_counts.values()):
        # For this case, forming groups of 5 is optimal
        copies_per_book = list(book_counts.values())[0]
        return int(copies_per_book * 5 * BASE_PRICE * 0.75)
    
    # For all other cases, run our optimization algorithm
    return optimize_grouping()
