from src.item import Item


class Mixin:

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self):
        return self.__language


class Keyboard(Item, Mixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


