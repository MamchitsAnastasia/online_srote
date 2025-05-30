class Product:
    """
    Класс для представления товара в магазине.

    Атрибуты:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара (с копейками)
        quantity (int): Количество товара в наличии (в штуках)
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Функция для инициализации экземпляра класса Product.

        Параметры:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
