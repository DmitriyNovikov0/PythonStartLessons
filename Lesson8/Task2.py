class DivisionByZero(Exception):
    def __init__(self, text):
        self._text = text

a = input('Введите делимое: ')
b = input('Введите делитель: ')
try:
    if not a.isdigit():
        raise DivisionByZero('Делимое должно быть числом')
    if not b.isdigit():
        raise DivisionByZero('Делитель должно быть числом')
    if int(b) == 0:
        raise DivisionByZero('Деление на ноль невозможно!')
    print(f'{a}/{b} = {float(a)/float(b)}')
except DivisionByZero as err:
    print(err)