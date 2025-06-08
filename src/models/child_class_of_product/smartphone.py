from src.models.product import Product


class Smartphone(Product):
    """
    Класс для представления смартфона в магазине.
    Наследует от класса Product и добавляет следующие атрибуты:
    - efficiency: Производительность
    - model: Модель
    - memory: Объем встроенной памяти
    - color: Цвет
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        """
        Переопределение строкового представления для Smartphone.
        """
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
                f"(Модель: {self.model}, Память: {self.memory}GB)")
