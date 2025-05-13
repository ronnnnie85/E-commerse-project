from src.product import Product


class Category:
    """Класс, представляющий категорию товаров.

    Атрибуты:
        name (str): Название категории
        description (str): Описание категории
        products (list[Product]): Список товаров в категории

    Атрибуты класса:
        category_count (int): Счетчик количества созданных категорий
        product_count (int): Счетчик общего количества товаров во всех категориях
    """

    name: str
    description: str
    __products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализирует новый объект категории.

        Args:
            name: Название категории
            description: Описание категории
            __products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию.

        Args:
            product (Product): Товар для добавления в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает форматированную строку со списком товаров категории.

        Формат строки для каждого товара:
        "Название, цена руб. Остаток количество шт."
        """
        res = []
        for product in self.__products:
            res.append(f"{product}\n")

        return "".join(res)

    @property
    def products_in_list(self) -> list:
        """Возвращает список товаров категории."""
        return self.__products

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        return f"{self.name}, количество продуктов: {sum([product.quantity for product in self.__products])} шт."
