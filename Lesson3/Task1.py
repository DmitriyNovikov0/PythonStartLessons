def my_func(a, b):
    """
    функция делит два аргумента
    :param a: первый аргумент - делимое
    :type a: float
    :param b: второй аргумент - делитель
    :type b: float
    :return: возвращает результат деления
    """
    return a / b

try:
    print(f"Ответ: {my_func(float(input('Введите делимое: ')), float(input('Введите делитель: ')))}")
except ZeroDivisionError:
    print('Ошибка - Деление на 0 ')
except ValueError:
    print('Вы ввели один из операндов не число')