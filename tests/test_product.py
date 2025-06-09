from unittest.mock import MagicMock, patch

import pytest

from src.models.child_class_of_product.lawn_grass import LawnGrass
from src.models.child_class_of_product.smartphone import Smartphone
from src.models.product import Product


def test_product_initialization(product_example1: Product) -> None:
    """
    Тест класса Product,
    проверяет корректность записи при инициализации экземпляра класса
    """
    assert product_example1.name == "Телефон3000"
    assert product_example1.description == "Смартфон хороший жесть"
    assert product_example1.price == 500.3
    assert product_example1.quantity == 10


def test_product_private_price_attribute(product_example1: Product) -> None:
    """
    Тест класса Product,
    проверяет, что атрибут цены действительно приватный
    """
    with pytest.raises(AttributeError):
        # Попытка доступа к приватному атрибуту
        print(product_example1.__price)


def test_price_getter(product_example1: Product) -> None:
    """
    Тест класса Product,
    проверяет корректность работы геттера цены
    """
    assert product_example1.price == 500.3


def test_price_setter_positive(product_example1: Product) -> None:
    """
    Тест класса Product,
    проверяет установку корректной цены
    """
    product_example1.price = 600.0
    assert product_example1.price == 600.0


def test_price_setter_negative_value(product_example1: Product, capsys: pytest.CaptureFixture[str]) -> None:
    """
    Тест класса Product,
    проверяет реакцию на попытку установить отрицательную цену
    """
    product_example1.price = -100.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_example1.price == 500.3  # Цена не изменилась


def test_price_setter_zero_value(product_example1: Product, capsys: pytest.CaptureFixture[str]) -> None:
    """
    Тест класса Product,
    проверяет реакцию на попытку установить нулевую цену
    """
    product_example1.price = 0.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_example1.price == 500.3  # Цена не изменилась


@patch("builtins.input", return_value="y")
def test_price_reduction_confirmation_yes(
    mock_input: MagicMock, product_example1: Product, capsys: pytest.CaptureFixture[str]
) -> None:
    """
    Тест класса Product,
    проверяет подтверждение понижения цены (пользователь согласен)
    """
    product_example1.price = 400.0
    captured = capsys.readouterr()
    assert "Цена успешно изменена на 400.0" in captured.out
    assert product_example1.price == 400.0


@patch("builtins.input", return_value="n")
def test_price_reduction_confirmation_no(
    mock_input: MagicMock, product_example1: Product, capsys: pytest.CaptureFixture[str]
) -> None:
    """
    Тест класса Product,
    проверяет отмену понижения цены (пользователь не согласен)
    """
    product_example1.price = 400.0
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert product_example1.price == 500.3  # Цена не изменилась


def test_price_increase_no_confirmation(product_example1: Product, capsys: pytest.CaptureFixture[str]) -> None:
    """
    Тест класса Product,
    проверяет, что при повышении цены подтверждение не запрашивается
    """
    product_example1.price = 600.0
    captured = capsys.readouterr()
    assert "Вы действительно хотите понизить цену" not in captured.out
    assert "Цена успешно изменена на 600.0" in captured.out
    assert product_example1.price == 600.0


def test_new_product_creation() -> None:
    """Тест класса Product на создание нового товара без дубликатов"""
    product_data = {
        "name": "Новый товар",
        "description": "Описание",
        "price": 100.0,
        "quantity": 5,
    }
    product = Product.new_product(product_data)
    assert product.name == "Новый товар"
    assert product.price == 100.0
    assert product.quantity == 5


def test_new_product_duplicate_merge() -> None:
    """Тест класса Product на объединение дубликатов при создании товара."""
    existing_product = Product("Телефон", "Описание", 500.0, 10)
    product_data = {
        "name": "телефон",
        "description": "Новое описание",
        "price": 600.0,
        "quantity": 5,
    }
    updated_product = Product.new_product(product_data, [existing_product])
    assert updated_product is existing_product
    assert updated_product.quantity == 15  # 10 + 5
    assert updated_product.price == 600.0  # Берется максимальная цена
    assert updated_product.description == "Новое описание"


def test_new_product_invalid_price() -> None:
    """Тест класса Product на обработку невалидной цены при создании товара."""
    product_data = {
        "name": "Товар",
        "description": "Описание",
        "price": -100.0,
        "quantity": 5,
    }
    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        Product.new_product(product_data)


def test_new_product_invalid_quantity() -> None:
    """Тест класса Product на обработку отрицательного количества при создании товара."""
    product_data = {
        "name": "Товар",
        "description": "Описание",
        "price": 100.0,
        "quantity": -5,
    }
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        Product.new_product(product_data)


def test_product_addition() -> None:
    """Тест класса Product на сложение двух продуктов (метод add)"""
    product1 = Product("Товар 1", "Описание 1", 100.0, 10)
    product2 = Product("Товар 2", "Описание 2", 200.0, 2)
    total = product1 + product2
    assert total == 1400.0  # 100*10 + 200*2


def test_product_addition_with_different_types() -> None:
    """Тест класса Product при попытке сложения продукта с объектом другого типа"""
    product = Product("Товар", "Описание", 100.0, 5)
    with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
        product + 100  # type: ignore


def test_product_addition_with_zero_quantity() -> None:
    """Тест класса Product на сложение продуктов с нулевым количеством"""
    product1 = Product("Товар 1", "Описание 1", 100.0, 0)
    product2 = Product("Товар 2", "Описание 2", 200.0, 5)
    assert product1 + product2 == 1000.0  # 100*0 + 200*5


def test_add_only_same_class_products() -> None:
    """Тест класса Product при попытке сложения только товаров одного класса"""
    phone1 = Smartphone("Phone1", "Desc", 1000, 2, 95.0, "A", 128, "Black")
    phone2 = Smartphone("Phone2", "Desc", 2000, 3, 98.0, "B", 256, "White")
    grass1 = LawnGrass("Grass1", "Desc", 50, 10, "Россия", "14 дней", "Green")
    grass2 = LawnGrass("Grass2", "Desc", 70, 5, "Беларусь", "10 дней", "Blue")

    # Корректное сложение
    assert phone1 + phone2 == 1000 * 2 + 2000 * 3
    assert grass1 + grass2 == 50 * 10 + 70 * 5

    # Некорректное сложение
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        phone1 + grass1

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        grass2 + phone2


def test_add_inherited_class_products() -> None:
    """Тест класса Product на сложение наследников Product между собой"""
    base_product1 = Product("Товар1", "Описание", 100, 2)
    base_product2 = Product("Товар2", "Описание", 200, 3)
    phone = Smartphone("Phone", "Desc", 1000, 1, 95.0, "X", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 50, 1, "Россия", "14 дней", "Green")

    # Базовые продукты можно складывать
    assert base_product1 + base_product2 == 100 * 2 + 200 * 3

    # Наследники не складываются с базовым классом
    with pytest.raises(TypeError):
        base_product1 + phone

    with pytest.raises(TypeError):
        grass + base_product2
