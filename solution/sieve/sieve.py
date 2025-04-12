def primes(limit):
    """
    Find all prime numbers less than or equal to the given limit using the Sieve of Eratosthenes.
    
    The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers
    up to a specified integer by marking the multiples of each prime, starting with 2.
    
    Args:
        limit (int): Upper limit for finding prime numbers
        
    Returns:
        list: A list of all prime numbers less than or equal to the limit
        
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    if limit < 2:
        return []
    
    # Start with all numbers marked as potentially prime
    is_prime = [True] * (limit + 1)
    # 0 and 1 are not prime
    is_prime[0] = is_prime[1] = False
    
    # Apply the Sieve of Eratosthenes
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    # Collect all prime numbers
    return [num for num in range(2, limit + 1) if is_prime[num]]
