from src.models.product import Product


def test_product_initialization(product_example1: Product) -> None:
    """
    Тест класса Product,
    проверяет корректность записи при инициализации экземпляра класса
    """
    assert product_example1.name == "Телефон3000"
    assert product_example1.description == "Смартфон хороший жесть"
    assert product_example1.price == 500.3
    assert product_example1.quantity == 10
