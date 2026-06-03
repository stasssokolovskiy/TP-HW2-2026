import pytest
from ingredient import Ingredient

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