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
    price: float
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
        self.price = price
        self.quantity = quantity
