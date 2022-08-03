from random import randint

with open("text_5_out.txt", 'w', encoding='utf-8') as out_f:
    for i in [randint(1, 100) for x in range(1, 10)]:
        print(f'{i} ', end='', file=out_f)

with open("text_5_out.txt", 'r', encoding='utf-8') as out_f:
    my_list = out_f.read().strip().split(' ')

print(f'Сумма чисел в файле равна: {sum([int(i) for i in my_list])}')