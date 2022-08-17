class Road:
    __WEIGHT = 25
    __THICKNESS = 5
    #__weight python регистрозависимый язык по этому можно объявить переменную в нижнем регистре с тем же названием
    #что и переменная в верхнем регистре, это будут две разные переменные.
    #вроде все что в верхнем регистре это как константа(хотя констант нет в python)

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__weight = width * length * self.__WEIGHT * self.__THICKNESS

    def get_weight(self):
        return self.__weight / 1000

r1 = Road(20, 5000)
print(f'Для данной дороги потребуеться {r1.get_weight()} тонн асфальта')



