from ingredient import Ingredient
from recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if not Recipe.is_valid_ratio(portions):
            raise ValueError("Количество порций должно быть положительным")
        recipe = recipe.scale(portions)
        self._items += [(ingredient, recipe.title) for ingredient in recipe.ingredients]

    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self) -> list[Ingredient]:
        quantity_by_key = {}
        for item in self._items:
            ingredient = item[0]
            key = (ingredient.name, ingredient.unit)
            if key in quantity_by_key:
                quantity_by_key[key] += ingredient.quantity
            else:
                quantity_by_key[key] = ingredient.quantity
        ingredients = [Ingredient(name, quantity, unit) for (name, unit), quantity in quantity_by_key.items()]
        ingredients.sort(key=lambda x: x.name)
        return ingredients
    
    def __add__(self, other: "ShoppingList") -> "ShoppingList":
        new = ShoppingList()
        new._items = self._items + other._items
        return new