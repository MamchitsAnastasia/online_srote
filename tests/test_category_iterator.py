import pytest

from src.models.category import Category
from src.models.product import Product


def test_category_iterator_basic_usage(category_example: Category) -> None:
    """Тест класса CategoryIterator для базового использования итератора категории"""
    products = list(category_example)
    assert len(products) == 2
    assert isinstance(products[0], Product)
    assert products[0].name == "Телефон3000"
    assert products[1].name == "Ноутбук66"


def test_category_iterator_empty_category() -> None:
    """Тест класса CategoryIterator итератора с пустой категорией"""
    empty_category = Category("Пустая", "Нет товаров", [])
    products = list(empty_category)
    assert len(products) == 0


def test_category_iterator_multiple_passes(category_example: Category) -> None:
    """Тест класса CategoryIterator для нескольких проходов по итератору"""
    first_pass = [p.name for p in category_example]
    second_pass = [p.name for p in category_example]
    assert first_pass == ["Телефон3000", "Ноутбук66"]
    assert first_pass == second_pass


def test_category_iterator_manual_usage(category_example: Category) -> None:
    """Тест класса CategoryIterator для ручного использования итератора"""
    iterator = iter(category_example)
    product1 = next(iterator)
    product2 = next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)
    assert product1.name == "Телефон3000"
    assert product2.name == "Ноутбук66"
