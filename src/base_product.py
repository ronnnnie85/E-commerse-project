from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс, определяющий интерфейс для классов продуктов."""

    @classmethod
    @abstractmethod  # pragma: no cover
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Абстрактный метод класса для создания нового экземпляра продукта.

        Args:
            *args: Произвольные позиционные аргументы для создания продукта.
            **kwargs: Произвольные именованные аргументы для создания продукта.
        """
        pass
