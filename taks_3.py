class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Атрибуты:
        :param name: название книги
        :param author: автор книги
        """

        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        """
        Атрибуты:
        :param pages: страницы бумажной книги
        """

        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга '{self.name}' с {self.pages} страницами. Автор {self.author}"


class AudioBook(Book):
    """ Дочерний класс аудио-книги. """

    def __init__(self, name: str, author: str, duration: float):
        """
        Атрибуты:
        :param duration: продолжительность аудиокниги
        """
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise ValueError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return f"Аудио-книга '{self.name}' продолжительностью {self.duration} часов. Автор {self.author}"
