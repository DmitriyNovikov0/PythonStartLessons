from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = float(param)

    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return self.param / 6.5 + 0.5

    def __str__(self):
        return 'Расход ткани для пошива пальто ' + str(self.param) + ' размера составит ' + str(round(self.fabric_consumption, 2)) + ' метра'

class Suit(Clothes):
    @property
    def fabric_consumption(self):
        return self.param * 2 + 0.3

v = input('Введите размер пальто: ')
coat = Coat(v)
#можно с переопределеием __str__
print(coat)
h = input('Введите рост в метрах: ')
suit = Suit(h)
#а можно и без
print(f'Расход ткани для пошива костюма составит {round(suit.fabric_consumption, 2)} метра')