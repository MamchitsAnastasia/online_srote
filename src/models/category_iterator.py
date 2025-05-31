from src.models.category import Category
from src.models.product import Product


class CategoryIterator:
    """
    Класс-итератор для перебора товаров в категории.
    """

    def __init__(self, category: Category):
        """
        Функция для инициализации экземпляра класса-итератора.

        Параметры:
            category: Объект категории для итерации
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """
        Функция возвращает сам объект итератора.
        """
        return self

    def __next__(self) -> Product:
        """
        Функция возвращает следующий товар в категории, пока товары не закончились.
        """
        products = self.category.products_list
        if self.index < len(products):
            product = products[self.index]
            self.index += 1
            return product
        raise StopIteration
