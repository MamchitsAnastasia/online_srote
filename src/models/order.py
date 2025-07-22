from src.models.base_item import BaseItem
from src.models.product import Product
from src.models.zero_quantity_error import ZeroQuantityError


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
        try:
            self.validate_quantity(quantity)  # Использую метод родительского класса
            if product.quantity == 0:
                raise ZeroQuantityError("Нельзя добавить товар с нулевым количеством в заказ")

            self.product = product
            self.quantity = quantity
            self._items = [self]
            print("Товар успешно добавлен в заказ")
        finally:
            print("Обработка добавления товара в заказ завершена")

    @property
    def total_cost(self) -> float:
        """Общая стоимость заказа"""
        return self.product.price * self.quantity

    def __repr__(self) -> str:
        return f"Order({self.product.name}, {self.quantity}, {self.total_cost} руб.)"
