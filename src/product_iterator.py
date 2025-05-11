from src.category import Category
from src.product import Product


class ProductIterator:
    category_obj: Category
    index: int

    def __init__(self, category_obj: Category) -> None:
        self.category_obj = category_obj
        self.index = 0


    def __iter__(self):
        self.index = 0
        return self


    def __next__(self):
        if self.index < len(self.category_obj.products_in_list):
            product = self.category_obj.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

