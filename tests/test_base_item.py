from typing import List, Union

from src.models.base_item import BaseItem
from src.models.order import Order
from src.models.product import Product


class MockItem(BaseItem):
    """Mock-класс для тестирования BaseItem."""

    def __init__(self, items: List[Union[Product, Order]]):
        super().__init__()
        self._items = items

    @property
    def total_cost(self) -> float:
        return sum(
            item.price * item.quantity if isinstance(item, Product) else item.total_cost for item in self._items
        )


def test_base_item_initialization(product_example1: Product, order_example: Order) -> None:
    """Тест инициализации абстрактного базового класса BaseItem"""
    mock_item = MockItem([product_example1, order_example])
    assert mock_item.items_count == 2
    assert mock_item.total_cost == (500.3 * 10) + (500.3 * 1)  # Продукт + заказ


def test_base_item_empty_items() -> None:
    """Тест абстрактного базового класса BaseItem с пустым списком элементов."""
    mock_item = MockItem([])
    assert mock_item.items_count == 0
    assert mock_item.total_cost == 0.0
    assert str(mock_item) == "MockItem (0 items, total: 0.0 руб.)"


def test_base_item_total_cost(product_example1: Product) -> None:
    """Тест абстрактного базового класса BaseItem при расчете общей стоимости."""
    mock_item = MockItem([product_example1])
    assert mock_item.total_cost == 500.3 * 10


def test_base_item_str_representation(product_example1: Product) -> None:
    """Тест абстрактного базового класса BaseItem при строковом представлении."""
    mock_item = MockItem([product_example1])
    expected_str = f"MockItem (1 items, total: {500.3 * 10} руб.)"
    assert str(mock_item) == expected_str


def test_base_item_items_count(product_example1: Product, order_example: Order) -> None:
    """Тест абстрактного базового класса BaseItem при подсчете количества элементов."""
    mock_item = MockItem([product_example1, order_example])
    assert mock_item.items_count == 2
