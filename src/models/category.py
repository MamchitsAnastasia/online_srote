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
        self.products = products
        # Увеличиваю счетчик категорий при создании нового объекта
        Category.category_count += 1
        # Увеличиваю счетчик уникальных товаров на количество товаров в категории
        Category.product_count += len(products)