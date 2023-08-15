import unittest
from unittest.mock import Mock
from src.static.diets import Diet
from src.controllers.recipecontroller import RecipeController

class TestGetRecipeReadiness(unittest.TestCase):
    def test_readiness_above_threshold(self):
        # Arrange
        recipe = {
            'diets': [Diet.VEGETARIAN],  # Use the Diet enum member
            # Add other recipe details as needed
        }
        available_items = {
            'quantity1': 5,
            'quantity2': 10,
            # Add other available items as needed
        }
        diet = Diet.VEGETARIAN  # Use the Diet enum member

        items_dao_mock = Mock()

        your_instance = RecipeController(items_dao=items_dao_mock)  # Instantiate your class here

        # Act
        readiness = your_instance.get_recipe_readiness(recipe, available_items, diet)

        # Assert
        self.assertIsNotNone(readiness)
        self.assertGreater(readiness, 0.1)



    def test_readiness_below_threshold(self):
        # Arrange
        recipe = {
            'diets': [Diet.VEGETARIAN],  # Use the Diet enum member
            # Add other recipe details as needed
        }
        available_items = {
            'quantity1': 1,
            'quantity2': 2,
            # Add other available items as needed
        }
        diet = Diet.VEGETARIAN  # Use the Diet enum member

        items_dao_mock = Mock()

        your_instance = RecipeController(items_dao=items_dao_mock)  # Instantiate your class here
        
        # Act
        readiness = your_instance.get_recipe_readiness(recipe, available_items, diet)

        # Assert
        self.assertIsNone(readiness)

    def test_recipe_not_compliant_with_diet(self):
        # Arrange
        recipe = {
            'diets': [Diet.VEGAN],  # Use the Diet enum member
            # Add other recipe details as needed
        }
        available_items = {
            'quantity1': 5,
            'quantity2': 10,
            # Add other available items as needed
        }
        diet = Diet.VEGETARIAN  # Use the Diet enum member
        
        items_dao_mock = Mock()

        your_instance = RecipeController(items_dao=items_dao_mock)  # Instantiate your class here
        
        # Act
        readiness = your_instance.get_recipe_readiness(recipe, available_items, diet)

        # Assert
        self.assertIsNone(readiness)

    def test_insufficient_ingredients(self):
        recipe = {
            'name': 'Test Recipe',
            'diets': ['vegan'],
            # ... other recipe data
        }
        available_items = {
            'ingredient1': 1,
            # ... other available items
        }
        diet = Diet(name='vegan')  # Assuming you have a Diet class defined
        
        result = self.your_instance.get_recipe_readiness(recipe, available_items, diet)
        self.assertIsNone(result)
        
if __name__ == '__main__':
    unittest.main()
