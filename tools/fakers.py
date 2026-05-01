import random
from faker import Faker

class Fake:
    """Класс генерации случайных тестовых данных на основе библиотеки Faker"""
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        """генерация случайного текста"""
        return self.faker.text()

    def uuid4(self) -> str:
        """Генерация случайного UUID4"""
        return self.faker.uuid4()

    def email(self) -> str:
        """Генерация случайного email"""
        return self.faker.email()

    def sentence(self) -> str:
        """Генерация случайного предложения"""
        return self.faker.sentence()

    def password(self) -> str:
        """Генерация случайного пароля"""
        return self.faker.password()

    def last_name(self) -> str:
        """Генерация случайной фамилии"""
        return self.faker.last_name()

    def first_name(self) -> str:
        """Генерация случайного имени"""
        return self.faker.first_name()

    def middle_name(self) -> str:
        """Генерация отчества"""
        # В ru_RU отчества доступны только с привязкой к полу
        return random.choice([self.faker.middle_name_male(), self.faker.middle_name_female()])

    def estimated_time(self) -> str:
        """Генерирует строку с предполаемым временем например '2 weeks'"""
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """Генерация случайного целого числа в диапазоне"""

        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """ Генерирует случайный максимальный балл в диапазоне от 50 до 100."""

        return self.integer(50, 100)

    def min_score(self) -> int:
        """ Генерирует случайный минимальный балл в диапазоне от 1 до 30."""

        return self.integer(1, 30)

# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker('ru_RU'))