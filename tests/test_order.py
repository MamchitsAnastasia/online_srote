import pytest

from src.models.order import Order
from src.models.product import Product


def test_order_initialization(product_example1: Product) -> None:
    """Тест корректной инициализации заказа."""
    order = Order(product_example1, 2)
    assert order.product == product_example1
    assert order.quantity == 2
    assert order.total_cost == 500.3 * 2


def test_order_invalid_quantity_zero(product_example1: Product) -> None:
    """Тест инициализации заказа с нулевым количеством."""
    with pytest.raises(ValueError, match="Количество товара должно быть положительным"):
        Order(product_example1, 0)


def test_order_invalid_quantity_negative(product_example1: Product) -> None:
    """Тест инициализации заказа с отрицательным количеством."""
    with pytest.raises(ValueError, match="Количество товара должно быть положительным"):
        Order(product_example1, -1)


def test_order_total_cost(product_example1: Product) -> None:
    """Тест расчета общей стоимости заказа."""
    order = Order(product_example1, 3)
    assert order.total_cost == 500.3 * 3


def test_order_repr(product_example1: Product) -> None:
    """Тест строкового представления заказа."""
    order = Order(product_example1, 2)
    expected_repr = f"Order({product_example1.name}, 2, {500.3 * 2} руб.)"
    assert repr(order) == expected_repr


def test_order_items_count(product_example1: Product) -> None:
    """Тест количества элементов в заказе (наследуется от BaseItem)."""
    order = Order(product_example1, 1)
    assert order.items_count == 1  # _items = [self]
