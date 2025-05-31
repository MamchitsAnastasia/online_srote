from typing import TYPE_CHECKING, Any, Iterator

if TYPE_CHECKING:
    from src.models.category import Category  # Импорт только для проверки типов

from src.models.product import Product


class CategoryIterator:
    """
    Класс-итератор для перебора товаров в категории.
    """

    def __init__(self, category: "Category"):  # type: ignore
        """
        Функция для инициализации экземпляра класса-итератора.

        Параметры:
            category: Объект категории для итерации
        """
        self.category = category
        self.index = 0

    def __iter__(self) -> Iterator[Product]:
        """
        Функция возвращает сам объект итератора.
        """
        return self

    def __next__(self) -> Any:
        """
        Функция возвращает следующий товар в категории, пока товары не закончились.
        """
        products = self.category.products_list
        if self.index < len(products):
            product = products[self.index]
            self.index += 1
            return product
        raise StopIteration
