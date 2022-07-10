list_products = []
product_count = 0

while True:
    s = input('Выбирете действие (1 - добавить товар. 2 - просмотреть список товаров. 3 - аналитика по товарам. q - Выход): ')
    if s == '1':
        product_name = input('Введите наименование товара: ')
        product_price = float(input('Введите стоимость товара: '))
        product_c = int(input('Введите количество товара: '))
        product_ed = input('Введите единицу измерения: ')
        product_count += 1
        list_products.append((product_count, {'название' : product_name, 'цена' : product_price, 'количество' : product_c, 'eд' : product_ed}))
    elif s == '2':
        for l1 in list_products:
            print(f'{l1[0]}. {l1[1]}')
    elif s == '3':
        list_name = []
        list_price = []
        list_c = []
        list_ed = []
        for l1 in list_products:
            list_name.append(l1[1].get('название'))
            list_price.append(l1[1].get('цена'))
            list_c.append(l1[1].get('количество'))
            list_ed.append(l1[1].get('eд'))

        print(f'название: {list_name}')
        print(f'цена: {list_price}')
        print(f'количество: {list_c}')
        print(f'ед: {set(list_ed)}') #что бы не повторялись значения воспользуемся множеством, как в методички 
    elif s == 'q':
        break
