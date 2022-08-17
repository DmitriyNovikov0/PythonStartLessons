#я если честно не доконца понял эту задачу, о многопоточности мы ничего не знаем,
#если бы каждый объект создавался в отдельном потоке и начинал работать было бы интеереснее
from time import sleep

class TrafficLight:
    nmb_tl = 1
    __color = ['красный', 'желтый', 'зеленый']
    __i = 0

    def __int__(self):
        TrafficLight.nmb_tl += 1

    def running(self):
        while True:
            print(f'на светофоре {TrafficLight.nmb_tl} горит {self.__color[self.__i]} свет')
            if self.__i == 0:
                sleep(7)
            elif self.__i == 1:
                sleep(2)
            elif self.__i == 2:
                sleep(5)
            self.__i += 1
            if self.__i > 2:
                self.__i = 0


l1 = TrafficLight()
l1.running()
#если бы каждый экземпляр класса запускался в одтьельном потоке было бы интереснее :)
# программа зациклиться в бесконечном цикле, дальнейших код не отработает в однопоточном приложении :)
l2 = TrafficLight()
l2.running()