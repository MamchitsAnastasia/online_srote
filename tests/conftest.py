import json
import os
from typing import Any, Callable

import pytest

from src.models.category import Category
from src.models.product import Product


@pytest.fixture
def product_example1() -> Product:
    """Фикстура для первого примера продукта"""
    return Product("Телефон3000", "Смартфон хороший жесть", 500.3, 10)


@pytest.fixture
def product_example2() -> Product:
    """Фикстура для второго примера продукта"""
    return Product("Ноутбук66", "Мощный ноутбук ну ваще", 1200.5, 5)


@pytest.fixture
def category_example(product_example1: Product, product_example2: Product) -> Category:
    """Фикстура для примера категории"""
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Электроника",
        "Гаджеты со странным описанием",
        [product_example1, product_example2],
    )


@pytest.fixture
def temp_json_file(tmp_path: Any) -> Callable[[list[dict[str, Any]]], str]:
    """Фикстура для временного JSON файла"""

    def make_temp_file(content: Any) -> str:
        file_path = os.path.join(tmp_path, "test_data.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f)
        return file_path

    return make_temp_file
