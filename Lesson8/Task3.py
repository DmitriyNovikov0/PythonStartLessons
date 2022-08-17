#делаю как написанно в методичке в подсказке - Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
class InputOnlyDigit(Exception):
    def __init__(self, text):
        self._text = text

dig_list = []
while True:
    try:
        a = input('Введите число(для выхода из цикла введите "stop"): ')
        if a == 'stop':
            break
        if not a.isdigit():
            raise InputOnlyDigit('Введенный символ должен быть числом!')
        else:
            dig_list.append(a)
    except InputOnlyDigit as err:
        print(err)

print([i for i in dig_list])