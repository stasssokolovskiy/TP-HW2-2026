from ingredient import Ingredient

class Recipe:
    def __init__(self, title:str, ingredients:list[Ingredient] = None):
        if ingredients is None:
            ingredients = []
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient:Ingredient):
        same_ingredients = [same for same in self.ingredients if same == ingredient]
        if same_ingredients:
            same_ingredients[0].quantity += ingredient.quantity
            return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float) -> "Recipe":
        new_ingredients = [Ingredient(own.name, own.quantity * ratio, own.unit) for own in self.ingredients]
        return Recipe(self.title, new_ingredients)
    
    def __len__(self) -> int:
        return len(self.ingredients)
    
    def __str__(self) -> str:
        return self.title + ":\n" + "\n".join(["\t" + str(item) for item in self.ingredients])