import json

from src.models.category import Category
from src.models.product import Product


def load_data_from_json(file_path: str) -> list[Category]:
    """
    Функция загружает данные из JSON файла и создает объекты Category и Product
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise ValueError(f"Файл {file_path} не найден")
    except json.JSONDecodeError:
        raise ValueError("Ошибка декодирования JSON")

    categories = []

    for category_data in data:
        # Устанавливаю значения по умолчанию для категории
        category_name = category_data.get("name", "")
        category_description = category_data.get("description", "")

        products = []
        for product_data in category_data.get("products", []):
            # Устанавливаю значения по умолчанию для товара
            try:
                product = Product(
                    name=product_data.get("name", ""),
                    description=product_data.get("description", ""),
                    price=float(product_data.get("price", 0.0)),
                    quantity=int(product_data.get("quantity", 0)),
                )
                products.append(product)
            except (ValueError, TypeError):
                continue

        category = Category(
            name=category_name, description=category_description, products=products
        )
        categories.append(category)

    return categories
