from unittest.mock import MagicMock, patch

import pytest

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
