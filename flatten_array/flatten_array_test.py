import unittest
from flatten_array import flatten

class FlattenArrayTest(unittest.TestCase):
    def test_empty_list(self):
        """Test that an empty list flattens to an empty list."""
        self.assertEqual(flatten([]), [])
    
    def test_single_value(self):
        """Test that a list with a single value flattens to a list with a single value."""
        self.assertEqual(flatten([1]), [1])
    
    def test_flat_list(self):
        """Test that a flat list flattens to the same list."""
        self.assertEqual(flatten([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_list_with_one_level_of_nesting(self):
        """Test flattening a list with one level of nesting."""
        self.assertEqual(flatten([1, [2, 3, 4], 5]), [1, 2, 3, 4, 5])
    
    def test_list_with_multiple_levels_of_nesting(self):
        """Test flattening a list with multiple levels of nesting."""
        self.assertEqual(flatten([1, [2, [3, 4], 5]]), [1, 2, 3, 4, 5])
    
    def test_list_with_deep_nesting(self):
        """Test flattening a deeply nested list."""
        self.assertEqual(
            flatten([0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]),
            [0, 2, 2, 3, 8, 100, 4, 50, -2]
        )
    
    def test_null_values_are_removed(self):
        """Test that None values are removed from the flattened list."""
        self.assertEqual(
            flatten([1, 2, None, 3, None, 4, 5, None]),
            [1, 2, 3, 4, 5]
        )
    
    def test_null_values_in_nested_lists_are_removed(self):
        """Test that None values in nested lists are removed."""
        self.assertEqual(
            flatten([1, [2, None, 3], 4]),
            [1, 2, 3, 4]
        )
    
    def test_nested_lists_with_only_null_values_result_in_empty_list(self):
        """Test that nested lists with only None values result in an empty list."""
        self.assertEqual(
            flatten([None, [[[None]]], None, None, [[None, None], None], None]),
            []
        )
    
    def test_mixed_types(self):
        """Test flattening a list with mixed types."""
        self.assertEqual(
            flatten([1, "a", [2, ["b", "c"], 3], 4.5, [5]]),
            [1, "a", 2, "b", "c", 3, 4.5, 5]
        )
    
    def test_tuple_input(self):
        """Test that the function works with tuple input."""
        self.assertEqual(
            flatten((1, (2, 3), 4)),
            [1, 2, 3, 4]
        )
    
    def test_mixed_tuple_and_list_input(self):
        """Test that the function works with mixed tuple and list input."""
        self.assertEqual(
            flatten([1, (2, [3, 4]), 5]),
            [1, 2, 3, 4, 5]
        )
    
    def test_example_from_instructions(self):
        """Test the example given in the instructions."""
        self.assertEqual(
            flatten([1, [2, 6, None], [[None, [4]], 5]]),
            [1, 2, 6, 4, 5]
        )


if __name__ == "__main__":
    unittest.main()