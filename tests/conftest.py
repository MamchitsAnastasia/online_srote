import pytest

from src.models.category import Category
from src.models.product import Product


@pytest.fixture
def product_example1():
    """Фикстура для первого примера продукта"""
    return Product("Телефон3000", "Смартфон хороший жесть", 500.3, 10)


@pytest.fixture
def product_example2():
    """Фикстура для второго примера продукта"""
    return Product("Ноутбук66", "Мощный ноутбук ну ваще", 1200.5, 5)


@pytest.fixture
def category_example(product_example1, product_example2):
    """Фикстура для примера категории"""
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Электроника",
        "Гаджеты со странным описанием",
        [product_example1, product_example2],
    )
