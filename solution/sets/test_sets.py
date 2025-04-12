import unittest
from sets import (clean_ingredients,
                  check_drinks,
                  categorize_dish,
                  tag_special_ingredients,
                  compile_ingredients,
                  separate_appetizers,
                  singleton_ingredients)


class ManualSetsTest(unittest.TestCase):
    
    def test_clean_ingredients(self):
        """Test removing duplicate ingredients."""
        dish_name = "Pasta with Tomatoes"
        ingredients = ["pasta", "tomatoes", "garlic", "tomatoes", "olive oil", "garlic", "basil"]
        expected = ("Pasta with Tomatoes", {"pasta", "tomatoes", "garlic", "olive oil", "basil"})
        
        self.assertEqual(clean_ingredients(dish_name, ingredients), expected)
        
    def test_check_drinks_cocktail(self):
        """Test that a drink with alcohol is categorized as a cocktail."""
        drink_name = "Mojito"
        ingredients = ["white rum", "mint", "lime juice", "sugar", "soda water"]
        
        self.assertEqual(check_drinks(drink_name, ingredients), "Mojito Cocktail")
        
    def test_check_drinks_mocktail(self):
        """Test that a drink without alcohol is categorized as a mocktail."""
        drink_name = "Virgin Mojito"
        ingredients = ["mint", "lime juice", "sugar", "soda water"]
        
        self.assertEqual(check_drinks(drink_name, ingredients), "Virgin Mojito Mocktail")
        
    def test_categorize_dish_vegan(self):
        """Test categorizing a vegan dish."""
        dish_name = "Simple Salad"
        ingredients = {"lettuce", "tomatoes", "olive oil", "vinegar", "salt"}
        
        self.assertEqual(categorize_dish(dish_name, ingredients), "Simple Salad: VEGAN")
        
    def test_tag_special_ingredients(self):
        """Test identifying allergens and special ingredients."""
        dish = ("Pasta with Seafood", ["pasta", "shrimp", "garlic", "tomatoes", "olive oil"])
        expected = ("Pasta with Seafood", {"shrimp", "garlic", "tomatoes"})
        
        self.assertEqual(tag_special_ingredients(dish), expected)
        
    def test_compile_ingredients(self):
        """Test combining ingredients from multiple dishes."""
        dishes = [
            {"pasta", "tomatoes", "garlic"},
            {"rice", "beans", "garlic"},
            {"bread", "butter", "jam"}
        ]
        expected = {"pasta", "tomatoes", "garlic", "rice", "beans", "bread", "butter", "jam"}
        
        self.assertEqual(compile_ingredients(dishes), expected)
        
    def test_separate_appetizers(self):
        """Test removing appetizers from a list of dishes."""
        dishes = ["Pasta", "Bruschetta", "Risotto", "Calamari", "Tiramisu"]
        appetizers = ["Bruschetta", "Calamari"]
        expected = ["Pasta", "Risotto", "Tiramisu"]
        
        self.assertEqual(sorted(separate_appetizers(dishes, appetizers)), sorted(expected))
        
    def test_singleton_ingredients(self):
        """Test finding ingredients that appear in only one dish."""
        dishes = [
            {"pasta", "tomatoes", "garlic"},
            {"pasta", "cheese", "garlic"},
            {"pasta", "basil", "olive oil"}
        ]
        # Ingredients that appear in more than one dish
        intersection = {"pasta", "garlic"}
        expected = {"tomatoes", "cheese", "basil", "olive oil"}
        
        self.assertEqual(singleton_ingredients(dishes, intersection), expected)


if __name__ == "__main__":
    unittest.main()
