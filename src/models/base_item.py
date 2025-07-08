from abc import ABC, abstractmethod
from typing import List, Union



class BaseItem(ABC):
    """
    Абстрактный базовый класс для элементов, содержащих товары.
    Объединяет общую функциональность для Заказов и Категорий.
    """

    @abstractmethod
    def __init__(self):
        self._items: List['Order | Product'] = []

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