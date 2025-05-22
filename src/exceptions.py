from typing import Any


class ProductError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args[0] if args else "Ошибка добавления продукта")


class ProductTypeError(ProductError):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args[0] if args else "Неправильный тип продукта")


class ProductZeroError(ProductError):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args[0] if args else "Нулевое количество продукта")
