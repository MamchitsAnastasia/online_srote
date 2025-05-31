from typing import Optional


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
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """
        Функция для строкового представления продукта в формате:
        Название продукта, XXX руб. Остаток: YYY шт.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Магический метод для сложения продуктов.
        Возвращает сумму общей стоимости двух продуктов.

        Параметры:
            other: Другой объект Product для сложения
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        """
        Геттер для получения цены товара.
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для установки цены товара с проверкой.
        Если цена <= 0, выводит сообщение об ошибке и не изменяет цену.

        Параметры:
            new_price: Новая цена товара
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            # Запрашиваем подтверждение на понижение цены
            confirmation = input(f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if confirmation.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price
        print(f"Цена успешно изменена на {new_price}")

    @classmethod
    def new_product(
        cls, product_data: dict, existing_products: Optional[list["Product"]] = None
    ) -> "Product":  # Отложенное определение класса
        """
        Класс-метод для создания нового товара из словаря.

        Параметры:
            product_data: Словарь с данными товара
            existing_products: Список существующих товаров для проверки дубликатов
        """
        if existing_products is None:
            existing_products = []
        # Извлекаю данные из словаря с проверкой наличия ключей
        name = product_data.get("name", "")
        description = product_data.get("description", "")
        price = float(product_data.get("price", 0.0))
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        quantity = int(product_data.get("quantity", 0))
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        # Проверяю наличие товара с таким же именем
        for existing_product in existing_products:
            if existing_product.name.lower() == name.lower():
                # Объединяю количество
                existing_product.quantity += quantity
                # Выбираю максимальную цену
                existing_product.price = max(existing_product.price, price)
                # Обновляю описание, если оно было передано
                if description:
                    existing_product.description = description
                return existing_product
        # Создаю и возвращаю новый объект Product
        return cls(name=name, description=description, price=price, quantity=quantity)
