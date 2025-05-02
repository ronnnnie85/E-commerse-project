from typing import Self

from mypy.stubgen import SelfTraverser


class Product:
    """Класс, представляющий товар.

    Attributes:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Цена товара.
        quantity (int): Количество единиц товара в наличии.
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует экземпляр класса Product.

        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена товара.
            quantity (int): Количество единиц товара в наличии.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params: dict) -> Self:
        return cls(**params)


    @property
    def price(self) -> float:
        return self.__price


    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


