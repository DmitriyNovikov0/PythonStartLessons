def my_func(a, b ,c):
    """
    функция принимает на вход 3 аргумента и возвращает сумму 2 наибольших аргументов
    :param a:
    :param b:
    :param c:
    :return:
    """
    tmp_list = [a, b, c]
    tmp_list.sort(reverse = True)
    return tmp_list[0] + tmp_list[1]

print(f'Сумма наибольших двух эллиментов =  {my_func(8, 1, 4)}')