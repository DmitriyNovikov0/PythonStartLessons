class Worker:
    __income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def set_income(self, wage, bonus):
        self.__income.update({'wage': wage, 'bonus': bonus})

    def get_income(self):
        return sum(self.__income.values())

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        super().set_income(wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.get_income()


p1 = Position('Иван', 'Иванов', 'Директор', 200000, 150000)
p2 = Position('Петров', 'Петр', 'Завхоз', 100000, 50000)
p3 = Position('Лена', 'Петрова', 'Уборщица', 60000, 5000)
print(f'{p1.get_full_name()} {p1.position} получает {p1.get_total_income()} рублей')
print(f'{p2.get_full_name()} {p2.position} получает {p2.get_total_income()} рублей')
print(f'{p3.get_full_name()} {p3.position} получает {p3.get_total_income()} рублей')
