from src.models.category import Category
from src.models.product import Product


def test_category_initialization(category_example, product_example1, product_example2):
    """
    Тест класса Category,
    проверяет корректность записи при инициализации экземпляра класса
    """
    assert category_example.name == "Электроника"
    assert category_example.description == "Гаджеты со странным описанием"
    assert len(category_example.products) == 2
    assert product_example1 in category_example.products
    assert product_example2 in category_example.products


def test_category_for_category_count(category_example):
    """Тест класса Category на подсчет количества категорий"""
    assert Category.category_count == 1
    Category("Новая категория", "Пустая категория", [])
    assert Category.category_count == 2


def test_category_for_product_count(category_example):
    """Тест класса Category на подсчет количества уникальных товаров"""
    assert Category.product_count == 2
    new_product = Product("Планшет3310", 'Планшет такой себе, конечно"', 800.0, 3)
    Category("Другая новая категория", "А это не пустая категория", [new_product])
    assert Category.product_count == 3
