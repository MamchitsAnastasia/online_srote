import pytest
from unittest.mock import MagicMock
from typing import Optional, List
from src.models.base_product import BaseProduct


class MockProduct(BaseProduct):
    """Mock-класс для тестирования BaseProduct."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        if not isinstance(other, MockProduct):
            raise TypeError("Можно складывать только объекты MockProduct")
        return self._price * self.quantity + other._price * other.quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = new_price

    @classmethod
    def new_product(
        cls, product_data: dict, existing_products: Optional[List["BaseProduct"]] = None
    ) -> "MockProduct":
        if existing_products is None:
            existing_products = []

        name = product_data.get("name", "")
        description = product_data.get("description", "")
        price = float(product_data.get("price", 0.0))
        quantity = int(product_data.get("quantity", 0))

        # Проверяем, есть ли уже такой товар
        for existing_product in existing_products:
            if existing_product.name.lower() == name.lower():
                # Обновляем существующий товар
                existing_product.description = description
                existing_product.price = price
                existing_product.quantity += quantity
                return existing_product  # Возвращаем существующий объект

        # Если не нашли — создаём новый
        return cls(name, description, price, quantity)


def test_base_product_initialization():
    """Тест инициализации mock-продукта."""
    product = MockProduct("Телефон", "Смартфон", 500.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 500.0
    assert product.quantity == 10


def test_base_product_str():
    """Тест строкового представления."""
    product = MockProduct("Телефон", "Смартфон", 500.0, 10)
    assert str(product) == "Телефон, 500.0 руб. Остаток: 10 шт."


def test_base_product_addition():
    """Тест сложения продуктов."""
    product1 = MockProduct("Телефон", "Смартфон", 500.0, 2)
    product2 = MockProduct("Ноутбук", "Игровой", 1000.0, 1)
    assert product1 + product2 == 500.0 * 2 + 1000.0 * 1


def test_base_product_addition_invalid_type():
    """Тест сложения с неверным типом."""
    product = MockProduct("Телефон", "Смартфон", 500.0, 2)
    with pytest.raises(TypeError, match="Можно складывать только объекты MockProduct"):
        product + 100  # type: ignore


def test_base_product_price_getter():
    """Тест геттера цены."""
    product = MockProduct("Телефон", "Смартфон", 500.0, 10)
    assert product.price == 500.0


def test_base_product_price_setter_valid():
    """Тест сеттера цены с корректным значением."""
    product = MockProduct("Телефон", "Смартфон", 500.0, 10)
    product.price = 600.0
    assert product.price == 600.0


def test_base_product_price_setter_invalid():
    """Тест сеттера цены с некорректным значением."""
    product = MockProduct("Телефон", "Смартфон", 500.0, 10)
    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        product.price = -100.0


def test_base_product_new_product():
    """Тест создания нового продукта через new_product."""
    product_data = {
        "name": "Телефон",
        "description": "Смартфон",
        "price": "500.0",
        "quantity": "10",
    }
    product = MockProduct.new_product(product_data)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 500.0
    assert product.quantity == 10


def test_base_product_new_product_with_existing():
    """Тест создания нового продукта с проверкой дубликатов."""
    existing_product = MockProduct("Телефон", "Старое описание", 400.0, 5)
    product_data = {
        "name": "Телефон",
        "description": "Новое описание",
        "price": "500.0",
        "quantity": "10",
    }
    updated_product = MockProduct.new_product(product_data, [existing_product])
    assert updated_product is existing_product
    assert updated_product.description == "Новое описание"
    assert updated_product.price == 500.0
    assert updated_product.quantity == 15