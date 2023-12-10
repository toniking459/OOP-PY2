import doctest


class Student:
    """класс , описывающий студента"""

    def __init__(self, average_grade: float, student_name: str, student_age: int):
        """
        Атрибуты:
        :param average_grade: средний балл студента
        :param student_name: имя студента
        :param student_age: возраст студента

        Примеры:
        >>> first_student = Student( 5.0, "Artem" , 19) # Инициализация объекта класса с параметрами
        """

        self.average_grade = average_grade
        self.student_name = student_name
        self.student_age = student_age

        if average_grade < 0:
            raise TypeError("Оценка не может быть меньше нуля")

        if student_age < 0:
            raise TypeError("Возраст студента не может быть меньше нуля")

        if not isinstance(student_name, str):
            raise TypeError("Имя должно быть типа string")

    def get_information(self) -> str:
        """метод получения информации о студенте

        return: Возвращает строку с тремя аргументами (имя, возраст, средний балл студента)


        """
        # return f"Информация о студенте:\nИмя:{self.student_name}\t| Возраст:{self.student_age}\t | Средний балл:{
        # self.average_grade}"

    def upd_avg_grade(self, new_average_grade) -> int:
        """метод, позволяющий изменить средний балл студента

        Атрибуты:
        :param new_average_grade: новый атрибут new_average_grade, задающий новый средний балл студента
        return: Возравщает строку с обновленным средним баллом студента


        """
        # self.average_grade = new_average_grade
        # return f"\nНовый средний балл студента:{self.average_grade}"

    def is_excellent_student(self) -> bool:
        """метод, позволяющий определитьь отличник ли определённый студент"""
        ...


class Library:
    """класс, описывающий библдиотеку"""

    def __init__(self, amount_of_books: int, books: list, staff: str):
        """
        Атрибуты:
        :param amount_of_books: количество книг в библиотеке (в штуках)
        :param books: сами книги , прдеставленные в виде списка
        :param staff: сотрудники библиотеки

        Примеры:
        >>> library = Library( 50000, ["А.П. Чехов - Пари"], "Anton") # создание экземляра класса в параметрами
        """

        self.amount_of_books = amount_of_books
        self.staff = staff
        self.books = books

        if amount_of_books < 0:
            raise TypeError("Ошибка! Количество книг не может быть отрицательным.")

        if not isinstance(staff, str):
            raise TypeError("Ошибка! Информация о персонале должна быть типа string.")

        if not isinstance(books, list):
            raise TypeError("Ошибка! Книги должны быть представлены в виде списка.")

    def add_book(self, new_book) -> None:
        """метод, позволяющирй добавлять нонвые книги в библиотеку

        :param new_book: книга, которая добавляется в библиотеку

        """

        ...

    def find_book(self) -> bool:
        """метод, позволяющзий найти книгу в библиотеке

        return: возвращает 1 если книга есть в библиотекек, 0 если книги в библиотеке не оказалось

        """

        ...

    def reserve_book(self) -> list:
        """метод, отвечающий за резевацию книг

        return: возвращает список зарезервированных книг

        """

        ...


class Car:
    """класс, описывающий автомобиль"""

    def __init__(self, brand: str, type_of_vehicle: str, horsepower: int):
        """
        Атрибуты:
        :param brand: марка автомобиля
        :param type_of_vehicle: тип автомобился (универсал, купе, ...)
        :param horsepower: количество лошадиных сил

        Пример:
        >>> first_car = Car("BMW", "Седан", 315) # инициализация объекта класса с параметрами
        """

        self.brand = brand
        self.type_of_vehicle = type_of_vehicle
        self.horsepower = horsepower

        if not isinstance(brand, str):
            raise TypeError("Ошибка! Бренд должен быть указан в виде строки!")

        if not isinstance(type_of_vehicle, str):
            raise TypeError("Ошибка! Тип автомобиля должен быть указан в виде строки!")

        if horsepower < 0:
            raise TypeError("Ошибка! Количество лошадиных сил не может быть отрицательным")

    def start_engine(self) -> None:
        """Метод для старта двигателя"""

        ...

    def stop_engine(self) -> None:
        """Метод для того, чтобы заглущить автомобиль"""

        ...

    def accelerate(self, speed_increase) -> int:
        """Метод ускорения автомобиля

        Атрибуты:
        :param speed_increase: величина, на которую увеличивается скорость автомобиля
        return: возвращает скорость автомобиля после ускорения

        """

        ...


if __name__ == "__main__":

    doctest.testmod()
    pass
