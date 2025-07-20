class ZeroQuantityError(Exception):
    """Класс-исключение для обработки попыток добавления товара с нулевым количеством"""
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"