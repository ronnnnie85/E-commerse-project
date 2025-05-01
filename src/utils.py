import json
from typing import Any, Dict, List

from src.category import Category
from src.product import Product


def read_data_json(file_path: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл и возвращает данные в виде списка словарей."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return list(json.load(file))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def load_data_from_json(file_path: str) -> List[Category]:
    """Создает объекты Category и Product из данных JSON."""
    data = read_data_json(file_path)

    if not data:
        return []

    categories = []
    required_fields = {"name", "description", "products"}

    for category_data in data:
        if not all(field in category_data for field in required_fields):
            continue

        products = [
            Product(**prod)
            for prod in category_data["products"]
            if all(key in prod for key in ["name", "description", "price", "quantity"])
        ]

        if products:
            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)

    return categories
