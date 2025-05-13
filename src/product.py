from typing import Any, Optional


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
    def new_product(cls, params: dict, list_products: Optional[list] = None) -> Any:
        """Создает новый товар или обновляет существующий в списке товаров.
        Если товар с таким именем уже существует в списке, увеличивает его количество
        и обновляет цену (если новая цена выше). В противном случае создает новый товар.

        Args:
            params (dict): Словарь с параметрами товара (name, description, price, quantity).
            list_products (Optional[list]): Список существующих товаров. По умолчанию None."""
        for product in list_products if list_products else []:
            if product.name == params.get("name"):
                product.quantity += params.get("quantity", 0)
                if price := params.get("price", 0) != product.price:
                    product.price = max(price, product.price)

                return product

        return cls(**params)

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Устанавливает новую цену товара.

        Если новая цена <= 0, выводит сообщение об ошибке.
        Если новая цена ниже текущей, запрашивает подтверждение.

        Args:
            price (float): Новая цена товара."""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if self.__price > price and input("Вы уверены что цена должна быть понижена?(y/n)").strip().lower() != "y":
                return

            self.__price = price

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Складывает общую стоимость товаров (цена * количество).
        Args:
            other (Product): Другой товар для сложения."""
        if type(self) is type(other):
            return round(float(self.price * self.quantity + other.price * other.quantity), 2)

        raise TypeError
