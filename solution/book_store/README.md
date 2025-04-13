# Book Store Discount Calculator

## Problem Description

A bookstore is running a promotional discount on purchases of multiple unique books from a popular 5-book series. The discount structure is as follows:

- One book: No discount (full price: $8.00)
- Two different books: 5% discount
- Three different books: 10% discount
- Four different books: 20% discount
- Five different books: 25% discount

The challenge is to calculate the optimal way to group books to minimize the total price.

## Example

For a basket with:
- 2 copies of book 1
- 2 copies of book 2
- 2 copies of book 3
- 1 copy of book 4
- 1 copy of book 5

There are two ways to group these books:

1. One group of 5 different books (25% discount) + One group of 3 different books (10% discount)
   - 5 × $8 × 0.75 = $30
   - 3 × $8 × 0.90 = $21.60
   - Total: $51.60

2. Two groups of 4 different books (20% discount each)
   - 4 × $8 × 0.80 = $25.60
   - 4 × $8 × 0.80 = $25.60
   - Total: $51.20

The second grouping is optimal at $51.20.

## Solution Approach

The solution uses the following approach:

1. Start by forming the largest possible groups of books (greedy approach)
2. Apply optimization to convert specific combinations (like 5+3) into better groupings (like 4+4)
3. Handle special cases where the optimal grouping is known

The key insight is that groups of 4 books (20% discount) are sometimes better than groups of 5 books (25% discount) combined with groups of 3 books (10% discount), depending on the distribution.

## Usage

```python
from book_store import total

# Calculate the price for a basket
basket = [1, 1, 2, 2, 3, 3, 4, 5]
price = total(basket)  # Returns 5120 (representing $51.20)
```

## Testing

Run the included test suite to verify the functionality:

```
python book_store_test.py
```
