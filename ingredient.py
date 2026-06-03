class Ingredient:
    def __init__(self, name:str, quantity:float, unit:str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self) -> float:
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity:float):
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity:.1f} {self.unit}"
    
    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity:.1f}, '{self.unit}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.name == other.name and self.unit == other.unit