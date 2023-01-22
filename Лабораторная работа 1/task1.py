from typing import Union
import doctest

class Meal:
    def __init__(self, name: str, cooking_time: Union[int, float], cooking_time_now: Union[int, float]):
        """
         Создание и подготовка к работе объекта "Блюдо"
         :param name: Название блюда
         :param cooking_time: Время приготовления
         :param cooking_time_now: Времени до готовности
         Примеры:
         >>> meal1 = Meal("Пицца Маргарита", 30, 20) # инициализация экземпляра класса
                """
        self.name = name
        if not isinstance(name, str):
            raise TypeError("Название блюда должно быть типа str")

        if not isinstance(cooking_time, (int, float)):
            raise TypeError("Время приготовления должно быть типа int или float")
        if not cooking_time > 0:
            raise ValueError("Время приготовления должно быть положительным числом")
        self.cooking_time = cooking_time

        if not isinstance(cooking_time_now, (int, float)):
            raise TypeError("Время должно быть типа int или float")
        if not cooking_time_now > 0:
            raise ValueError("Время должно быть положительным числом")
        self.cooking_time_now = cooking_time_now

    def test1_meal(self) -> bool:
        """
        Функция которая проверяет готово ли блюдо
        :return: Готово ли блюдо
        Примеры:
        >>> meal1 = Meal("Пицца Маргарита", 30, 20)
        >>> meal1.test_meal()
        """
        ...

    def test2_meal(self) -> bool:
        """
        Функция которая проверяет не испортилось ли блюдо
        :return: Испортилось ли блюдо
        Примеры:
        >>> meal1 = Meal("Пицца Маргарита", 30, 40)
        >>> meal1.test_meal()
        """
        ...

class Menu:
    def __init__(self, name_meals: dict, number_of_dishes: int, number_of_pages: int):
        """
        Создание и подготовка к работе объекта "Меню"
        :param name_meals: Название блюда и его количество
        :param number_of_dishes: Количество блюд
        :param number_of_pages: Количество страниц
        Примеры:
        >>> menu1 = Menu({"Карбонара": 9}, 100, 120) # инициализация экземпляра класса
        """
        self.name_meals = {} if name_meals is None else name_meals

        if not isinstance(number_of_dishes, int):
            raise TypeError("Количество блюд должно быть типа int")
        if not number_of_dishes > 0:
            raise ValueError("Количество блюд должно быть положительным числом")
        self.number_of_dishes = number_of_dishes

        if not isinstance(number_of_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if not number_of_pages > 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.number_of_pages = number_of_pages

    def get_meal(self, name: str):
        """
        Функция которая создает словарь с блюдом и его количеством
        :param guests_new: Новые посетители
        :raise ValueError: Если количество новых посетителей превышает свободное место в рестаране, то вызываем ошибку
        """
        if name not in self.name_meals:
            raise ValueError("Бюлюда нет в меню")
        if self.name_meals[name] == 0:
            raise ValueError("Бюлюда нет в наличии")
        ...


class Restaurant:
    def __init__(self, numbers_of_menu: int, capacity: int, guests_now: int):
        """
        Создание и подготовка к работе объекта "Меню"
        :param numbers_of_menu: Количество меню
        :param capacity: Вместимость
        :param guests_now: Количество посетителей в данный момент
        Примеры:
        >>> restaurant1 = Restaurant(100, 100, 60) # инициализация экземпляра класса
        """
        if not isinstance(numbers_of_menu, int):
            raise TypeError("Количество меню должно быть типа int")
        if not numbers_of_menu > 0:
            raise ValueError("Количество меню должно быть положительным числом")
        self.numbers_of_menu = numbers_of_menu

        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость должно быть типа int")
        if not capacity > 0:
            raise ValueError("Вместимость должно быть положительным числом")
        self.capacity = capacity

        if not isinstance(guests_now, (int, float)):
            raise TypeError("Количество посетителей должно быть типа int")
        if not guests_now > 0:
            raise ValueError("Количество посетителей должно быть положительным числом")
        self.guests_now = guests_now
        if guests_now > capacity:
            raise ValueError("Количество посетителей должно быть меньше вместимости")

    def increment_guests_now(self, guests_new: int) -> None:
        """
        Функция которая добавляет количество посетителей в данный момент
        :param guests_new: Новые посетители
        :raise ValueError: Если количество новых посетителей превышает свободное место в рестаране, то вызываем ошибку
               Примеры:
        >>> restaurant1 = Restaurant(20, 40, 21)
        >>> restaurant1.increment_guests_now(12)
               """
        if not isinstance(guests_new, int):
            raise TypeError("Новые посетители должны быть типа int")
        if guests_new < 0:
            raise ValueError("Новые посетители должны быть положительным числом")
        ...

    def subrtacting_guests_now(self, guests_lose: int) -> None:
        """
        Функция которая теряет количество посетителей в данный момент
         :param guests_lose: Ушедшие посетители
        :raise ValueError: Количество оставшихся должно быть больше либо равно нулю
               Примеры:
        >>> restaurant1 = Restaurant(20, 40, 21)
        >>> restaurant1.subrtacting_guests_now(12)
               """
        if not isinstance(guests_lose, int):
            raise TypeError("Ушедшие посетители должны быть типа int")
        if guests_lose < 0:
            raise ValueError("Ушедшие посетители должны быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()