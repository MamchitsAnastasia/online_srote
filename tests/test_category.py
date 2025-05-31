import pytest

from src.models.category import Category
from src.models.product import Product


def test_category_initialization(
    category_example: Category, product_example1: Product, product_example2: Product
) -> None:
    """
    Тест класса Category,
    проверяет корректность записи при инициализации экземпляра класса
    """
    assert category_example.name == "Электроника"
    assert category_example.description == "Гаджеты со странным описанием"
    assert len(category_example.products.split("\n")) == 2  # Разбиваю строку на список
    assert "Телефон3000" in category_example.products
    assert "Ноутбук66" in category_example.products


def test_category_for_category_count(category_example: Category) -> None:
    """Тест класса Category на подсчет количества категорий"""
    assert Category.category_count == 1
    Category("Новая категория", "Пустая категория", [])
    assert Category.category_count == 2


def test_category_for_product_count(category_example: Category) -> None:
    """Тест класса Category на подсчет количества уникальных товаров"""
    assert Category.product_count == 2
    new_product = Product("Планшет3310", "Планшет такой себе, конечно", 800.0, 3)
    Category("Другая новая категория", "А это не пустая категория", [new_product])
    assert Category.product_count == 3


def test_private_products_attribute(category_example: Category) -> None:
    """
    Тест класса Category,
    проверяет, что атрибут __products действительно приватный
    """
    with pytest.raises(AttributeError):
        # Попытка доступа к приватному атрибуту
        print(category_example.__products)


def test_products_getter_format(category_example: Category) -> None:
    """
    Тест класса Category,
    проверяет формат вывода геттера products
    """
    products_output = category_example.products
    assert isinstance(products_output, str)
    lines = products_output.split("\n")
    assert len(lines) == 2
    assert "руб." in lines[0]
    assert "Остаток:" in lines[0]


def test_add_product_method(category_example: Category) -> None:
    """
    Тест класса Category,
    проверяет работу метода add_product
    """
    initial_count = len(category_example.products.split("\n"))
    new_product = Product("Новый товар", "Описание", 100.0, 5)
    category_example.add_product(new_product)
    assert len(category_example.products.split("\n")) == initial_count + 1
    assert "Новый товар" in category_example.products


def test_empty_category() -> None:
    """
    Тест класса Category,
    проверяет работу с пустой категорией
    """
    empty_category = Category("Пустая", "Нет товаров", [])
    assert empty_category.products == ""
    assert len(empty_category.products.split("\n")) == 1  # Пустая строка дает один элемент при split
