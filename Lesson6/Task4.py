class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Текущая скорость у {self.name}  {self.speed} км'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость у машины {self.name} = {self.speed} км')

        if self.speed > 40:
            return f'Скорость у {self.name} выше, чем разрешено для автомобиля'
        else:
            return f'Скорость у {self.name} = {self.speed}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость у рабочей машины {self.name} = {self.speed} км')

        if self.speed > 60:
            return f'Скорость у {self.name} выше, чем разрешено для рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} автомобиль не полицейский'


audi = SportCar(100, 'Красного', 'Audi', False)
oka = TownCar(30, 'Белого', 'Oka', False)
lada = WorkCar(70, 'Зеленого', 'Lada', True)
ford = PoliceCar(110, 'Голубого',  'Ford', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, тогда {audi.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name} {lada.color} цвета')
print(f'{audi.name} полицейский автомобиль? {audi.is_police}')
print(f'{lada.name} полицейский автомобиль? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())