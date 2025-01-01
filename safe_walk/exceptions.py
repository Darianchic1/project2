"""
Файл для хранения ошибок
"""

class BadPath(Exception):
    """
    Ошибка неверного пути
    """
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class BadFenceCoord(Exception):
    """
    Ошибка неверного формата координат
    """
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class BadWindowName(Exception):
    """
    Ошибка неверного имени окна
    """
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
