inp_str = input('Введите строку: ')

my_list = inp_str.split(' ')
i = 0
for s in my_list:
    i += 1
    print(f'{i}. {s if len(s) < 10 else s[:10]}')