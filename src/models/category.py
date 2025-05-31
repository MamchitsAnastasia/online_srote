from typing import Iterator

from src.models.category_iterator import CategoryIterator
from src.models.product import Product


class Category:
    """
    Класс для представления категории товаров в магазине.

    Атрибуты:
        name (str): Название категории товаров
        description (str): Описание категории товаров
        products (list[Product]): Список товаров категории
    """

    # Атрибуты класса
    category_count = 0  # Общее количество категорий
    product_count = 0  # Общее количество уникальных товаров

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Функция для инициализации экземпляра класса Product.

        Параметры:
            name: Название категории товаров
            description: Описание категории товаров
            products: Список товаров категории
        """
        self.name = name
        self.description = description
        self.__products = products
        # Увеличиваю счетчик категорий при создании нового объекта
        Category.category_count += 1
        # Увеличиваю счетчик уникальных товаров на количество товаров в категории
        # Счётчик для списка товаров при инициализации класса.
        Category.product_count += len(products)

    def __str__(self) -> str:
        """
        Функция для строкового представления категории в формате:
        Название категории, количество продуктов: XXX шт.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> Iterator[Product]:
        """
        Функция возвращает итератор для товаров категории.
        """
        return CategoryIterator(self)

    def add_product(self, product: Product) -> None:
        """
        Функция добавляет товар в категорию.

        Параметры:
            product: Объект класса Product для добавления
        """
        self.__products.append(product)
        # Увеличиваю счетчик товаров
        # Счётчик для товаров, добавленных через метод
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для вывода списка товаров в заданном формате:
        Название продукта, XXX руб. Остаток: YYY шт.
        """
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> list[Product]:
        """Геттер для получения списка продуктов (для итератора)"""
        return self.__products
