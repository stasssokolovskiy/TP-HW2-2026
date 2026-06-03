# Система управления рецептами
В проекте реализованны 4 класса:
* Ingredient хранит продукт или компонент блюда.
* Recipe хранит рецепт блюда
* ShoppingList хранит список покупок нужных для рецептов
* DietaryRecipe хранит рецепт и диетическую категорию

## Установка
Вам потребуется версия `python` не ниже `3.10`.

Клонируйте репозиторий и установите зависимости.

```bash
git clone https://github.com/stasssokolovskiy/TP-HW2-2026
cd TP-HW2-2026
pip install -r requirements.txt
pytest
```

## Использование
Для использования выполните импорты:
```python
from ingredient import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList
from dietary_recipe import DietaryRecipe
```

Для тестирования выполните `pytest` в корне проекта.

## Автор
Соколовский Станислав Андреевич ББИ2506