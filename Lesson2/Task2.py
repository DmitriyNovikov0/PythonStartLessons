i = 0
my_list = []

while True:
    str_tmp = input(f'Ведите {i}-й эллемент списка (закончить заполнение списка введите "q"): ')
    if str_tmp == 'q':
        break
# хотя можно было и без else
    else:
        i += 1
        my_list.append(str_tmp)

print(f'Исходный список \n{my_list}\n')
for i in range(0, len(my_list), 2):
    if i + 1 == len(my_list):
        break
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(f'Список после изминения \n{my_list}')