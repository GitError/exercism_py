import unittest
from dicts import (
    create_inventory,
    add_items,
    decrement_items,
    remove_item,
    list_inventory
)


class InventoryTest(unittest.TestCase):
    def test_create_inventory(self):
        self.assertEqual(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]),
                        {"coal": 1, "wood": 2, "diamond": 3})
        self.assertEqual(create_inventory([]), {})
        self.assertEqual(create_inventory(["iron", "iron", "iron"]), {"iron": 3})

    def test_add_items(self):
        self.assertEqual(add_items({"coal": 1}, ["wood", "iron", "coal", "wood"]),
                        {"coal": 2, "wood": 2, "iron": 1})
        self.assertEqual(add_items({}, ["coal", "coal"]), {"coal": 2})
        self.assertEqual(add_items({"wood": 2, "gold": 1}, []), {"wood": 2, "gold": 1})

    def test_decrement_items(self):
        self.assertEqual(
            decrement_items({"coal": 3, "diamond": 1, "iron": 5}, 
                           ["diamond", "coal", "iron", "iron"]),
            {"coal": 2, "diamond": 0, "iron": 3})
        self.assertEqual(
            decrement_items({"coal": 2, "wood": 1, "diamond": 2}, 
                           ["coal", "coal", "wood", "wood", "diamond"]),
            {"coal": 0, "wood": 0, "diamond": 1})
        self.assertEqual(decrement_items({"iron": 1}, []), {"iron": 1})
        self.assertEqual(decrement_items({"silver": 0}, ["silver"]), {"silver": 0})

    def test_remove_item(self):
        self.assertEqual(remove_item({"coal": 2, "wood": 1, "diamond": 2}, "coal"),
                        {"wood": 1, "diamond": 2})
        self.assertEqual(remove_item({"coal": 2, "wood": 1, "diamond": 2}, "gold"),
                        {"coal": 2, "wood": 1, "diamond": 2})
        self.assertEqual(remove_item({}, "silver"), {})

    def test_list_inventory(self):
        expected = [('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
        actual = list_inventory({"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0})
        # Sort both lists for consistent comparison
        self.assertEqual(sorted(actual), sorted(expected))
        self.assertEqual(list_inventory({"coal": 0, "wood": 0}), [])


if __name__ == "__main__":
    unittest.main()
