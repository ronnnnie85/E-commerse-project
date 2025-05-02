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
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self) -> str:
        res = []
        for product in self.__products:
            res.append(f"{product.name}, {product.price} руб. Остаток {product.quantity} шт.\n")

        return "".join(res)


