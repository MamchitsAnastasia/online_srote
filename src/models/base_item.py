from abc import ABC, abstractmethod
from typing import List

from src.models.zero_quantity_error import ZeroQuantityError


class BaseItem(ABC):
    """
    Абстрактный базовый класс для элементов, содержащих товары.
    Объединяет общую функциональность для Заказов и Категорий.
    """

    def __init__(self) -> None:
        self._items: List["Order | Product"] = []

    def validate_quantity(self, quantity: int) -> None:
        """Проверяет, что количество товара больше нуля"""
        if quantity <= 0:
            raise ZeroQuantityError("Количество товара должно быть положительным")

    @property
    @abstractmethod
    def total_cost(self) -> float:
        """Абстрактное свойство для расчета общей стоимости"""
        pass

    @property
    def items_count(self) -> int:
        """Количество элементов (товаров/заказов)"""
        return len(self._items)

    def __str__(self) -> str:
        """Строковое представление"""
        return f"{self.__class__.__name__} ({self.items_count} items, total: {float(self.total_cost)} руб.)"
