from abc import ABC, abstractmethod
from typing import List, Union
from src.models.product import Product
from src.models.order import Order


class BaseItem(ABC):
    """
    Абстрактный базовый класс для элементов, содержащих товары.
    Объединяет общую функциональность для Заказов и Категорий.
    """

    @abstractmethod
    def __init__(self):
        self._items: List[Union[Product, Order]] = []

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
        return f"{self.__class__.__name__} ({self.items_count} items, total: {self.total_cost} руб.)"