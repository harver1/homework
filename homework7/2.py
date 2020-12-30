#  Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
#  проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
#  У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
#  V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def expense(self,):
        pass


class Coat(Clothes):

    def __init__(self, size, name=None):
        self.name = name
        self.size = size

    @property
    def expense(self):
        return round((self.size/6.5 + 0.5), 2)


class Suit(Clothes):

    def __init__(self, height, name=None):
        self.name = name
        self.height = height

    @property
    def expense(self):
        return round((self.height * 2 + 0.3), 2)


nike = Coat(48, 'nike')
adidas = Suit(5, 'adidas')
print(nike.expense)
print(adidas.expense)
print(nike.expense + adidas.expense)

