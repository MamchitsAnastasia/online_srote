from abc import ABC, abstractmethod
from typing import Optional, Any


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для представления товара в магазине.
    Определяет общий интерфейс для всех продуктов.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Абстрактный метод инициализации продукта.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Абстрактный метод для строкового представления продукта.
        """
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """
        Абстрактный метод для сложения продуктов.
        """
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """
        Абстрактный геттер для цены товара.
        """
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """
        Абстрактный сеттер для цены товара.
        """
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict, existing_products: Optional[list["BaseProduct"]] = None) -> "BaseProduct":
        """
        Абстрактный класс-метод для создания нового товара.
        """
        pass
