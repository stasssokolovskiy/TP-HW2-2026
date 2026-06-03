import pytest
from ingredient import Ingredient
from recipe import Recipe

class TestIngredient:
    def test_init(self):
        name = "Вода"
        quantity = 1.
        unit = "л"
        ingredient = Ingredient(name, quantity, unit)
        assert ingredient.name == name
        assert ingredient.quantity == quantity
        assert ingredient.unit == unit
    
    def test_str(self):
        name = "Вода"
        quantity = 1.
        unit = "л"
        ingredient = Ingredient(name, quantity, unit)
        assert str(ingredient) == "Вода: 1.0 л"

    def test_eq(self):
        name = "Вода"
        quantity = 1.
        unit = "л"
        origin = Ingredient(name, quantity, unit)
        another_quantity = Ingredient(name, 2., unit)
        another_name = Ingredient("Молоко", quantity, unit)
        another_unit = Ingredient(name, quantity, "г")
        assert origin == another_quantity
        assert origin != another_name
        assert origin != another_unit

class TestRecipe:
    def test_init(self):
        ingred_list = [Ingredient("Вода", 1., "л")]
        recipe = Recipe("Water", ingred_list)
        assert recipe.title == "Water"
        list_from_recipe = recipe.ingredients
        assert len(list_from_recipe) == 1
        first = list_from_recipe[0]
        assert first.name == "Вода"
        assert first.quantity == 1.
        assert first.unit == "л"
    
    def test_add_ingredient(self):
        recipe = Recipe("Water")
        recipe.add_ingredient(Ingredient("Вода", 5., "л"))

        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0] == Ingredient("Вода", 1., "л")
        assert recipe.ingredients[0].quantity == 5.

        recipe.add_ingredient(Ingredient("Вода", 1., "л"))

        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0] == Ingredient("Вода", 1., "л")
        assert recipe.ingredients[0].quantity == 6.

    def test_scale(self):
        recipe = Recipe("Water")
        recipe.add_ingredient(Ingredient("Вода", 5., "л"))
        double_recipe = recipe.scale(2)

        assert len(recipe.ingredients) == 1
        origin = recipe.ingredients[0]
        assert origin == Ingredient("Вода", 1., "л")
        assert origin.quantity == 5.

        assert len(double_recipe.ingredients) == 1
        double = double_recipe.ingredients[0]
        assert double == Ingredient("Вода", 1., "л")
        assert double.quantity == 10.

    def test_scale_exception_for_invalid_ratio(self):
        recipe = Recipe("Water")
        recipe.add_ingredient(Ingredient("Вода", 5., "л"))
        with pytest.raises(ValueError):
            recipe.scale(0)

    def test_len(self):
        recipe = Recipe("Water")
        assert len(recipe) == 0
        recipe.add_ingredient(Ingredient("Вода", 5., "л"))
        assert len(recipe) == 1
        recipe.add_ingredient(Ingredient("Вода", 5., "л"))
        assert len(recipe) == 1