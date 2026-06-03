from ingredient import Ingredient
from recipe import Recipe

class DietaryRecipe(Recipe):
    def __init__(self, title:str, diet_type:str, ingredients:list[Ingredient] = None):
        self.diet_type = diet_type
        super().__init__(title, ingredients)
    
    def scale(self, ratio: float) -> "DietaryRecipe":
        recipe = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, recipe.ingredients)
    
    def __str__(self) -> str:
        return f"[{self.diet_type}] {super().__str__()}"