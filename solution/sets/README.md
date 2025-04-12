# Sets Exercise - Catering Company Functions

This exercise implements a collection of Python functions to help a catering company with organizing, shopping, prepping, and serving for a cooking club event.

## Functions Overview

### 1. `clean_ingredients(dish_name, dish_ingredients)`
Removes duplicate ingredients from ingredient lists to prevent purchasing excess items.

**Parameters:**
- `dish_name`: String containing the name of the dish
- `dish_ingredients`: List of ingredients for the dish

**Returns:** 
- Tuple with dish name and de-duplicated set of ingredients

### 2. `check_drinks(drink_name, drink_ingredients)`
Checks if a drink contains alcohol and labels it as either a "Cocktail" or "Mocktail".

**Parameters:**
- `drink_name`: String with the name of the drink
- `drink_ingredients`: List of ingredients in the drink

**Returns:**
- String with drink name followed by "Mocktail" or "Cocktail"

### 3. `categorize_dish(dish_name, dish_ingredients)`
Categorizes dishes for guests with different dietary needs (Vegan, Vegetarian, Paleo, Keto, or Omnivore).

**Parameters:**
- `dish_name`: String with the name of the dish
- `dish_ingredients`: Set of ingredients for the dish

**Returns:**
- String with dish name followed by its category

### 4. `tag_special_ingredients(dish)`
Tags ingredients that require special attention due to allergies or dietary restrictions.

**Parameters:**
- `dish`: Tuple with dish name and list of ingredients

**Returns:**
- Tuple with dish name and set of special ingredients

### 5. `compile_ingredients(dishes)`
Creates a master list of ingredients for shopping and ordering purposes.

**Parameters:**
- `dishes`: List of dish ingredient sets

**Returns:**
- Set of all unique ingredients from all dishes

### 6. `separate_appetizers(dishes, appetizers)`
Separates main dishes from bite-sized appetizers to be served on trays.

**Parameters:**
- `dishes`: List of dish names
- `appetizers`: List of appetizer names

**Returns:**
- List of dish names that are not appetizers

### 7. `singleton_ingredients(dishes, intersection)`
Identifies ingredients that only appear in one dish within a category.

**Parameters:**
- `dishes`: List of ingredient sets
- `intersection`: Set of ingredients that appear in multiple dishes

**Returns:**
- Set of ingredients that appear in only one dish

## Data Categories

The exercise uses several predefined categories from the `sets_categories_data.py` file:
- `VEGAN`: Set of vegan ingredients
- `VEGETARIAN`: Set of vegetarian ingredients
- `PALEO`: Set of paleo diet ingredients
- `KETO`: Set of ketogenic diet ingredients
- `OMNIVORE`: Set of omnivore ingredients
- `ALCOHOLS`: Set of alcoholic ingredients
- `SPECIAL_INGREDIENTS`: Set of allergens and special ingredients to be tracked
