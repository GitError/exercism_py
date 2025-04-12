import unittest
from dict_methods import (
    add_item,
    read_notes, 
    update_recipes,
    sort_entries,
    send_to_store,
    update_store_inventory
)
from dict_methods_test_data import (
    add_item_data,
    read_notes_data,
    update_recipes_data,
    sort_entries_data,
    send_to_store_data,
    update_store_inventory_data
)
from collections import OrderedDict


class DictMethodsTest(unittest.TestCase):
    
    def test_add_item(self):
        """Test add_item function with various inputs."""
        for variant, (input_data, expected) in enumerate(add_item_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                current_cart, items_to_add = input_data
                actual_result = add_item(current_cart, items_to_add)
                error_msg = (f'Called add_item({current_cart}, {items_to_add}). '
                            f'The function returned {actual_result}, but the tests '
                            f'expected: {expected} once the items were added.')
                self.assertEqual(actual_result, expected, msg=error_msg)
    
    def test_read_notes(self):
        """Test read_notes function with various inputs."""
        for variant, (input_data, expected) in enumerate(read_notes_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = read_notes(input_data)
                error_msg = (f'Called read_notes({input_data}). '
                            f'The function returned {actual_result}, but the tests '
                            f'expected: {expected}.')
                self.assertEqual(actual_result, expected, msg=error_msg)
    
    def test_update_recipes(self):
        """Test update_recipes function with various inputs."""
        for variant, (input_data, expected) in enumerate(update_recipes_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = update_recipes(input_data[0], input_data[1])
                error_msg = (f'Called update_recipes({input_data[0]}, {input_data[1]}). '
                            f'The function returned {actual_result}, but the tests '
                            f'expected: {expected} once the recipes were updated.')
                self.assertEqual(actual_result, expected, msg=error_msg)
    
    def test_sort_entries(self):
        """Test sort_entries function with various inputs."""
        for variant, (input_data, expected) in enumerate(sort_entries_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = sort_entries(input_data)
                error_msg = (f'Called sort_entries({input_data}). '
                            f'The function returned {actual_result}, but the tests '
                            f'expected: {expected} once the cart was sorted.')
                self.assertEqual(actual_result, expected, msg=error_msg)
    
    def test_send_to_store(self):
        """Test send_to_store function with various inputs."""
        for variant, (input_data, expected) in enumerate(send_to_store_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = send_to_store(input_data[0], input_data[1])
                error_msg = (f'Called send_to_store({input_data[0]}, {input_data[1]}). '
                            f'The function returned {actual_result}, but the tests '
                            f'expected: {expected} as the fulfillment cart.')
                # Convert to OrderedDict for consistent comparison
                self.assertEqual(OrderedDict(actual_result), OrderedDict(expected), msg=error_msg)
    
    def test_update_store_inventory(self):
        """Test update_store_inventory function with various inputs."""
        for variant, (input_data, expected) in enumerate(update_store_inventory_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = update_store_inventory(input_data[0], input_data[1])
                error_msg = (f'Called update_store_inventory({input_data[0]}, {input_data[1]}). '
                            f'The function returned {actual_result}, but the tests '
                            f'expected: {expected} once the inventory was updated.')
                self.assertEqual(actual_result, expected, msg=error_msg)


if __name__ == '__main__':
    unittest.main()
