import csv
import math

from src.exceptions import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if issubclass(self.__class__, Item) and issubclass(other.__class__, Item):
            return self.quantity + other.quantity
        raise TypeError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name: str) -> None:
        """
        Считывает список товаров из файла
        @param file_name: имя файла
        """
        try:
            with open(file_name, "r") as f:
                reader = csv.DictReader(f)
                cls.all.clear()
                for row in reader:
                    cls(row['name'], float(row['price']), int(row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {file_name}")
        except Exception:
            raise InstantiateCSVError(f"Файл {file_name} поврежден")


    @staticmethod
    def string_to_number(string: str):
        """
        Преобразует строку в число
        @param string: число в стороком представлении
        @return: число
        """
        return math.floor(float(string))
