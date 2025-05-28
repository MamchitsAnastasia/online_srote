import pytest
import os

from src.json_importer import load_data_from_json
from src.models.category import Category
from src.models.product import Product


def test_load_valid_data(temp_json_file):
    """Тест функции load_data_from_json для загрузки корректных данных"""
    test_data = [
        {
            "name": "Тестовая категория",
            "description": "Описание категории",
            "products": [
                {
                    "name": "Товар 1",
                    "description": "Описание 1",
                    "price": 100.0,
                    "quantity": 10,
                }
            ],
        }
    ]

    file_path = temp_json_file(test_data)
    categories = load_data_from_json(file_path)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Тестовая категория"
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Товар 1"


def test_load_empty_products(temp_json_file):
    """Тест функции load_data_from_json для загрузки категории без товаров"""
    test_data = [{"name": "Пустая категория", "description": "", "products": []}]

    file_path = temp_json_file(test_data)
    categories = load_data_from_json(file_path)

    assert len(categories) == 1
    assert len(categories[0].products) == 0


def test_missing_fields(temp_json_file):
    """Тест функции load_data_from_json для обработки отсутствующих полей"""
    test_data = [
        {
            "name": "Категория с неполными данными",
            "products": [{"name": "Товар без цены", "quantity": 5}],
        }
    ]

    file_path = temp_json_file(test_data)
    categories = load_data_from_json(file_path)

    assert categories[0].description == ""  # Проверка значения по умолчанию
    product = categories[0].products[0]
    assert product.description == ""  # Проверка значения по умолчанию
    assert product.price == 0.0  # Проверка значения по умолчанию


def test_invalid_data_types(temp_json_file):
    """Тест функции load_data_from_json для обработки неверных типов данных"""
    test_data = [
        {
            "name": "Категория с некорректными данными",
            "products": [
                {
                    "name": "Товар 1",
                    "price": "сто рублей",  # Не число
                    "quantity": "пять",  # Не число
                },
                {"name": "Товар 2", "price": 200.0, "quantity": 3},
            ],
        }
    ]

    file_path = temp_json_file(test_data)
    categories = load_data_from_json(file_path)

    # Проверяем, что только один товар был загружен (второй с корректными данными)
    assert len(categories[0].products) == 1
    assert categories[0].products[0].name == "Товар 2"


def test_file_not_found():
    """Тест функции load_data_from_json для обработки отсутствующего файла"""
    with pytest.raises(ValueError, match="не найден"):
        load_data_from_json("nonexistent_file.json")


def test_invalid_json(temp_json_file):
    """Тест функции load_data_from_json для обработки некорректного JSON"""
    file_path = os.path.join(
        temp_json_file.__closure__[0].cell_contents, "invalid.json"
    )
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("{invalid json}")

    with pytest.raises(ValueError, match="декодирования"):
        load_data_from_json(file_path)
