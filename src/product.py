from typing import Self, Optional


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
    def new_product(cls, params: dict, list_products: Optional[list] = None) -> Self:
        if list_products:
            for product in list_products:
                if product.name == params.get("name"):
                    price = params.get("price", 0)
                    product.quantity += params.get("quantity", 0)
                    if product.price != price:
                        product.price = max(price, product.price)

                    return product

        return cls(**params)


    @property
    def price(self) -> float:
        return self.__price


    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if self.__price > price and input("Вы уверены что цена должна быть понижена?(y/n)").strip().lower() != "y":
                return

            self.__price = price


