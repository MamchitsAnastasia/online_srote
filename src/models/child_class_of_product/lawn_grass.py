from src.models.product import Product


class LawnGrass(Product):
    """
    Класс для представления газонной травы в магазине.
    Наследует от класса Product и добавляет следующие атрибуты:
    - country: Страна-производитель
    - germination_period: Срок прорастания
    - color: Цвет
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """
        Переопределение строкового представления для LawnGrass.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. (Страна: {self.country}, Срок прорастания: {self.germination_period})"