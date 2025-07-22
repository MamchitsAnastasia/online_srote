class ZeroQuantityError(Exception):
    """Класс-исключение для обработки попыток добавления товара с нулевым количеством"""

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен") -> None:
        """
        Функция инициализации класса ZeroQuantityError
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """
        Функция возвращает строковое представление ошибки (сообщение об ошибке)
        """
        return f"{self.message}"
