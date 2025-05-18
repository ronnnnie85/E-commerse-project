from src.product import Product
from src.product_mixin import ProductMixin


class Smartphone(Product, ProductMixin):
    """Класс, представляющий смартфон как товар в магазине.

    Наследует базовый функционал класса Product и добавляет специфичные
    для смартфонов атрибуты.

    Attributes:
        efficiency (float): Эффективность (производительность)
        model (str): Модель смартфона
        memory (int): Объем памяти в ГБ
        color (str): Цвет устройства
    """

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует экземпляр смартфона.

        Args:
            name: Название смартфона
            description: Описание
            price: Цена
            quantity: Количество в наличии
            efficiency: Производительность
            model: Модель
            memory: Объем памяти (ГБ)
            color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
