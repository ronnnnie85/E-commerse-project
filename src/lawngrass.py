from src.product import Product
from src.product_mixin import ProductMixin


class LawnGrass(Product, ProductMixin):
    """Класс, представляющий товар - газонную траву.

    Наследует базовый функционал класса Product и добавляет специфичные атрибуты.

    Attributes:
            country (str): Страна-производитель травы
            germination_period (str): Период прорастания
            color (str): Цвет травы
    """

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует экземпляр газонной травы.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество в наличии
            country: Страна-производитель
            germination_period: Период прорастания
            color: Цвет травы
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
