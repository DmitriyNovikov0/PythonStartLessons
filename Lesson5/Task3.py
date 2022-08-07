my_dict = {}

with open("text_3.txt", "r", encoding='utf-8') as my_f:
    my_list = my_f.readlines()

for line in my_list:
    key, value = line.split(' ')
    my_dict.update({key: float(value)})

print(f'Средняя зарплата составляет: {sum(my_dict.values()) / len(my_dict)}')
print(f'Зарплату менее 20000 получают:')
for i in my_dict:
    if my_dict[i] < 20000:
        print(f'{i} получает {my_dict[i]}')