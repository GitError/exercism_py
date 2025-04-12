import unittest
from sets import (clean_ingredients,
                  check_drinks,
                  categorize_dish,
                  tag_special_ingredients,
                  compile_ingredients,
                  separate_appetizers,
                  singleton_ingredients)
from sets_test_data import (recipes_with_duplicates, 
                           recipes_without_duplicates, 
                           all_drinks, 
                           drink_names, 
                           dishes_categorized,
                           dishes_to_special_label, 
                           dishes_labeled, 
                           ingredients_only,
                           dishes_and_appetizers, 
                           dishes_cleaned, 
                           dishes_and_overlap,
                           backup_singletons)


class SetsTest(unittest.TestCase):

    def test_clean_ingredients(self):
        """Test cleaning ingredient lists by removing duplicates."""
        for recipe_in, recipe_expected in zip(recipes_with_duplicates, recipes_without_duplicates):
            dish_name, ingredients = recipe_in
            expected_dish_name, expected_ingredient_set = recipe_expected[1], recipe_expected[2]
            
            result = clean_ingredients(dish_name, ingredients)
            self.assertTrue(
                isinstance(result, tuple), 
                msg=f"Expected a tuple, but got {type(result)}"
            )
            
            self.assertEqual(
                result[0], expected_dish_name, 
                msg=f"Expected dish name '{expected_dish_name}', but got '{result[0]}'"
            )
            
            self.assertEqual(
                result[1], expected_ingredient_set, 
                msg=f"Expected ingredients {expected_ingredient_set}, but got {result[1]}"
            )

    def test_check_drinks(self):
        """Test correct labeling of drinks as cocktails or mocktails."""
        for drink_in, expected_name in zip(all_drinks, drink_names):
            drink_name, ingredients = drink_in
            result = check_drinks(drink_name, ingredients)
            self.assertEqual(
                result, expected_name, 
                msg=f"Expected '{expected_name}', but got '{result}'"
            )

    def test_categorize_dish(self):
        """Test categorizing dishes based on their ingredients."""
        for dish in recipes_without_duplicates:
            dish_name, ingredients_set = dish[1], dish[2]
            result = categorize_dish(dish_name, ingredients_set)
            self.assertIn(
                result, dishes_categorized, 
                msg=f"'{result}' is not a valid dish categorization"
            )

    def test_tag_special_ingredients(self):
        """Test identifying special ingredients that need labeling."""
        for dish, expected in zip(dishes_to_special_label, dishes_labeled):
            result = tag_special_ingredients(dish)
            self.assertEqual(
                result, expected, 
                msg=f"Expected {expected}, but got {result}"
            )

    def test_compile_ingredients(self):
        """Test compiling a master list of ingredients from multiple dishes."""
        for ingredient_group in ingredients_only:
            result = compile_ingredients(ingredient_group)
            expected = set().union(*ingredient_group)
            self.assertEqual(
                result, expected, 
                msg=f"Expected {expected}, but got {result}"
            )

    def test_separate_appetizers(self):
        """Test separating appetizers from the main dish list."""
        for (dishes, appetizers), expected in zip(dishes_and_appetizers, dishes_cleaned):
            result = sorted(separate_appetizers(dishes, appetizers))
            self.assertEqual(
                result, sorted(expected), 
                msg=f"Expected {sorted(expected)}, but got {result}"
            )

    def test_singleton_ingredients(self):
        """Test finding ingredients that appear in only one dish."""
        for (dishes, intersection), expected in zip(dishes_and_overlap, backup_singletons):
            result = singleton_ingredients(dishes, intersection)
            self.assertEqual(
                result, expected, 
                msg=f"Expected {expected}, but got {result}"
            )


if __name__ == "__main__":
    unittest.main()
