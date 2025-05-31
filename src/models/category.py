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
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(products_list)
