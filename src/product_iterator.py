from typing import Any

from src.category import Category


class ProductIterator:
    """Итератор для последовательного перебора товаров в категории.

    Позволяет итерироваться по товарам категории один за другим.

    Attributes:
        category_obj (Category): Объект категории, по товарам которой происходит итерация.
        index (int): Текущий индекс позиции итератора в списке товаров.
    """

    category_obj: Category
    index: int

    def __init__(self, category_obj: Category) -> None:
        """Инициализирует итератор для указанной категории товаров.

        Args:
            category_obj (Category): Категория товаров, по которой будет происходить итерация.
        """
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        """Возвращает сам итератор для использования в цикле for."""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Возвращает следующий товар в категории."""
        if self.index < len(self.category_obj.products_in_list):
            product = self.category_obj.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
