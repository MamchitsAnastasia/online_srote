from src.models.base_item import BaseItem
from src.models.product import Product


class Order(BaseItem):
    """
    Класс Заказ, содержащий информацию о купленном товаре.
    Наследует от BaseItem.
    """

    def __init__(self, product: Product, quantity: int):
        """
        :param product: Товар (объект класса Product)
        :param quantity: Количество товара
        """
        super().__init__()
        if quantity <= 0:
            raise ValueError("Количество товара должно быть положительным")
        self.product = product
        self.quantity = quantity
        self._items = [self]  # Инициализируем список с текущим заказом

    @property
    def total_cost(self) -> float:
        """Общая стоимость заказа"""
        return self.product.price * self.quantity

    def __repr__(self) -> str:
        return f"Order({self.product.name}, {self.quantity}, {self.total_cost} руб.)"
