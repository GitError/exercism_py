"""Performance testing for the dict_methods module."""

import timeit
from collections import Counter

def original_add_item(current_cart, items_to_add):
    """Original implementation of add_item."""
    updated_cart = current_cart.copy()
    
    for item in items_to_add:
        if item in updated_cart:
            updated_cart[item] += 1
        else:
            updated_cart[item] = 1
            
    return updated_cart

def optimized_add_item(current_cart, items_to_add):
    """Optimized implementation of add_item using Counter."""
    updated_cart = current_cart.copy()
    item_counts = Counter(items_to_add)
    
    for item, count in item_counts.items():
        updated_cart[item] = updated_cart.get(item, 0) + count
            
    return updated_cart

def test_performance():
    """Compare performance of original vs optimized implementations."""
    # Create test data
    current_cart = {f'item{i}': i for i in range(1000)}
    items_to_add = [f'item{i%2000}' for i in range(10000)]
    
    # Test original implementation
    original_time = timeit.timeit(
        lambda: original_add_item(current_cart, items_to_add), 
        number=100
    )
    
    # Test optimized implementation
    optimized_time = timeit.timeit(
        lambda: optimized_add_item(current_cart, items_to_add), 
        number=100
    )
    
    print(f"Original implementation: {original_time:.6f} seconds")
    print(f"Optimized implementation: {optimized_time:.6f} seconds")
    print(f"Improvement: {(original_time - optimized_time) / original_time * 100:.2f}%")
    
    # Validate results are the same
    original_result = original_add_item(current_cart, items_to_add)
    optimized_result = optimized_add_item(current_cart, items_to_add)
    assert original_result == optimized_result, "Implementations produce different results!"

if __name__ == "__main__":
    test_performance()
