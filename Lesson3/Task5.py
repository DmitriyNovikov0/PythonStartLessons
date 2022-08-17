my_sum = 0
stop_flag = False

def func_sum(in_str):
    if in_str.find('q') != -1:
        in_str = in_str.split('q')[0].strip() # обрезаем строку до символа q(вообще это разбиение, но мы возьмем только первую часть)
        global stop_flag
        stop_flag = True
    my_list = in_str.split(' ')
    return sum([int(x) for x in my_list])

while not stop_flag:
    try:
        my_sum +=  func_sum(input('Введите строку цифр разделенных пробелом(символ для выхода "q"): '))
    except ValueError:
        print('ошибка ввода! программа принимает только числа разделенные пробелом и символ q - конец ввода')
    print(f'Сумма чисел равна: {my_sum}')

