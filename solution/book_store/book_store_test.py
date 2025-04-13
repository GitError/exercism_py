import unittest
from book_store import total

class BookStoreTest(unittest.TestCase):
    """Tests for the book_store module."""
    
    def test_empty_basket(self):
        """Test that an empty basket returns zero price."""
        basket = []
        self.assertEqual(total(basket), 0)
    
    def test_single_book(self):
        """Test that a single book costs 800 cents."""
        basket = [1]
        self.assertEqual(total(basket), 800)
    
    def test_two_same_books(self):
        """Test that two copies of the same book cost 1600 cents (no discount)."""
        basket = [1, 1]
        self.assertEqual(total(basket), 1600)
    
    def test_two_different_books(self):
        """Test that two different books get a 5% discount."""
        basket = [1, 2]
        self.assertEqual(total(basket), 1520)  # 2 * 800 * 0.95
    
    def test_three_different_books(self):
        """Test that three different books get a 10% discount."""
        basket = [1, 2, 3]
        self.assertEqual(total(basket), 2160)  # 3 * 800 * 0.90
    
    def test_four_different_books(self):
        """Test that four different books get a 20% discount."""
        basket = [1, 2, 3, 4]
        self.assertEqual(total(basket), 2560)  # 4 * 800 * 0.80
    
    def test_five_different_books(self):
        """Test that five different books get a 25% discount."""
        basket = [1, 2, 3, 4, 5]
        self.assertEqual(total(basket), 3000)  # 5 * 800 * 0.75
    
    def test_two_groups_of_four(self):
        """Test that two groups of four books are correctly discounted."""
        basket = [1, 1, 2, 2, 3, 3, 4, 5]
        self.assertEqual(total(basket), 5120)  # 2 groups of 4 at 20% discount: 8 * 800 * 0.80
    
    def test_two_groups_of_four_with_different_distribution(self):
        """Test another distribution that should produce two groups of four."""
        basket = [1, 1, 2, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 5120)
    
    def test_group_of_four_plus_group_of_two(self):
        """Test that a group of four plus a group of two is correctly discounted."""
        basket = [1, 1, 2, 2, 3, 4]
        self.assertEqual(total(basket), 4080)  # 4 books at 20% + 2 books at 5%
    
    def test_two_copies_of_each_book(self):
        """Test that two copies of each book are optimally grouped."""
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 6000)  # 2 groups of 5 at 25% discount
    
    def test_various_combinations(self):
        """Test various combinations to ensure optimal grouping."""
        test_cases = [
            ([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5], 8120),
            ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5], 10000),
            ([1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5], 10240),
        ]
        
        for basket, expected in test_cases:
            with self.subTest(basket=basket):
                self.assertEqual(total(basket), expected)
    
    def test_edge_cases(self):
        """Test edge cases with complex groupings."""
        # 22 books with specific distribution requiring optimal grouping
        basket = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 14560)

if __name__ == '__main__':
    unittest.main()
