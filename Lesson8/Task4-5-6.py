from abc import ABC, abstractmethod

class InputErrorDate(Exception):
    def __init__(self, text):
        self._text = text

class Equipment(ABC):
    def __init__(self, type, model, price):
        self._type = type
        self._model = model
        self._price = price

    @abstractmethod
    def get_info_str(self):
        pass

    @abstractmethod
    def get_info_dict(self):
        pass

class Printer(Equipment):
    def __init__(self, model, price, laser = False, color = False):
        super().__init__('Принтер', model, price)
        self._laser = laser
        self._color = color

    def __str__(self):
        return f'{self._type} Модель: {self._model}. Цена: {self._price}. Характеристики: (цветной - {self._color}, лазерный - {self._laser})'

    def get_info_str(self):
        #тут после удаления лезут ошибки, если раскоментировать принт первый раз проходит нормально, при повторном удалении лезут ошибки
        #print(self)
        return f'{self._type} Модель: {self._model}. Цена: {self._price}. Характеристики: (цветной - {self._color}, лазерный - {self._laser})'

    def get_info_dict(self):
        return {'type': 'Принтер', 'model': self._model, 'price': self._price, 'color': self._color, 'laser': self._laser}

class Scanner(Equipment):
    def __init__(self, model, price, scaner_format):
        super().__init__('Сканер', model, price)
        self._scaner_format = scaner_format

    def __str__(self):
        return f'{self._type} Модель: {self._model}. Цена: {self._price}. Характеристики: (сканер формата: {self._scaner_format})'

    def get_info_str(self):
        #тут после удаления лезут ошибки, если раскоментировать принт первый раз проходит нормально, при повторном удалении лезут ошибки
        #print(self)
        return f'{self._type} Модель: {self._model}. Цена: {self._price}. Характеристики: (сканер формата: {self._scaner_format})'

    def get_info_dict(self):
        return {'type': 'Сканер', 'model': self._model, 'price': self._price, 'format': self._scaner_format}

class Copier(Equipment):
    def __init__(self, model, price, copir_format, color = False):
        super().__init__('Ксерокс', model, price)
        self._copir_format = copir_format
        self._color = color

    def get_info_str(self):
        #тут после удаления лезут ошибки, если раскоментировать принт первый раз проходит нормально, при повторном удалении лезут ошибки
        #print(self)
        return f'{self._type} Модель: {self._model}. Цена: {self._price}. Характеристики: (цветной - {self._color}, формата ксерокса: {self._copir_format})'

    def get_info_dict(self):
        return {'type': 'Копир', 'model': self._model, 'price': self._price, 'color': self._color, 'format': self._copir_format}

class EquipmentWarehouse:
    def __init__(self, count=0):
        self._max_count = count
        self._equipment_in_stock = []

    def warehouse_receipt(self, equipment, quantity):
        self._equipment_in_stock.append({'equipment': equipment, 'quantity': quantity})
        print('Позиция добавлена на склад.')

    def equipment_in_warehouse(self):
        return [i.get('equipment').get_info_str() + '. Количество на складе: ' + str(i.get('quantity')) + ' шт.' for i in self._equipment_in_stock]

    def remove_equipment(self, model, quantity):
        #не лучший алгоритм поиска но для учебного проекта пойдет, нужно индексировать
        for i, dict_str in enumerate(self._equipment_in_stock):
            if dict_str.get('equipment')._model == model:
                if dict_str.get('quantity') < quantity:
                    print(f'Ошибка! На складе всего {dict_str.get("quantity")} позиций этого товара, Вы пытаетесь переместить {quantity} позиций')
                else:
                    self._equipment_in_stock[i]['quantity'] = dict_str.get('quantity') - quantity
                    print(f'На складе осталось {dict_str["quantity"]} позиций {self._equipment_in_stock[i].get("equipment")._model}, перемещенно {quantity} позиций')
                    break # так как удалили можно цикл завершать, немного не правильный алгоритм поиска
            else:
                print('На складе не найденна введеная Вам модель орг.техники!')

    def add_equipment(self):
        while True:
            in_str = input(
                'Выберите действие: 1 - добавить Принтер, 2 - добавить Сканер, 3 - добавить Ксерокс, q - предедущие меню: ')
            if in_str.upper() == 'Q':
                break
            elif in_str == '1':
                unit = chek_enter('принтер')
                # это всего лишь пример, проверку можно организовать куда красивее
                if unit.get('model') is None:
                    continue
                if self._max_count < unit.get('quantity'):
                    raise InputErrorDate(f'На складе не хватает места! возможно разместить только {self._max_count} позиций товара')
                printer_ = Printer(unit.get('model'), unit.get('price'), unit.get('color'), unit.get('laser'))
                self._max_count -= unit.get('quantity')
                self.warehouse_receipt(printer_, unit.get('quantity'))
            elif in_str == '2':
                unit = chek_enter('сканер')
                if unit.get('model') is None:
                    continue
                if self._max_count < unit.get('quantity'):
                    raise InputErrorDate(f'На складе не хватает места! возможно разместить только {self._max_count} позиций товара')
                scaner_ = Scanner(unit.get('model'), unit.get('price'), unit.get('scaner_format'))
                self._max_count -= unit.get('quantity')
                self.warehouse_receipt(scaner_, unit.get('quantity'))
            elif in_str == '3':
                unit = chek_enter('ксерокс')
                if unit.get('model') is None:
                    continue
                if self._max_count < unit.get('quantity'):
                    raise InputErrorDate(f'На складе не хватает места! возможно разместить только {self._max_count} позиций товара')
                copier_ = Copier(unit.get('model'), unit.get('price'), unit.get('copier_format'), unit.get('scaner_format', unit.get('color')))
                self._max_count -= unit.get('quantity')
                self.warehouse_receipt(copier_, unit.get('quantity'))

def chek_enter(name_equipment):
    out_dict = {}
    try:
        model_= input(f'Введите модель {name_equipment}а: ')
        price_ = float(input(f'Введите цену {name_equipment}а: '))
        quantity_ = int(input(f'Введите количество поступивших на склад {name_equipment}ов: '))
        if name_equipment == 'принтер':
            color_ = input(f'{name_equipment} цветной? y/n: ').upper()
            laser_ = input(f'{name_equipment} дазерный? y/n: ').upper()
            if not(color_ == 'Y' or color_ == 'N') and (laser_ == 'Y' or laser_ == 'N'):
                raise InputErrorDate('Не корректный ввод данных!')
            else:
                out_dict.update({'model': model_, 'price': price_, 'quantity': quantity_, 'color': True if color_ == 'Y' else False,
                                 'laser': True if laser_ == 'Y' else False})
        elif name_equipment == 'сканер':
            scaner_format_ = input(f'Формат {name_equipment}а(A3/A4) : ')
            out_dict.update({'model': model_, 'price': price_, 'quantity': quantity_, 'scaner_format': scaner_format_})
        elif name_equipment == 'ксерокс':
            color_ = input(f'{name_equipment} цветной? y/n: ').upper()
            copier_format_ = input(f'Формат {name_equipment}а(A3/A4) : ')
            if not (color_ == 'Y' or color_ == 'N'):
                raise InputErrorDate('Не корректный ввод данных!')
            else:
                out_dict.update({'model': model_, 'price': price_, 'quantity': quantity_, 'copier_format': copier_format_,'color': True if color_ == 'Y' else False})
    except:
        print('Не корректный ввод данных!')
        out_dict.clear()
    return out_dict


warehouse = EquipmentWarehouse(100) # создаем склад со 100 позициями для оргтехники
while True:
    in_str = input('Выберите действие: 1 - просмотр остатков на складе, 2 - добовление товара на склад, 3 - удаление/перемещение со склада, q- Выход: ')
    if in_str.upper() == 'Q':
        break
    elif in_str == '1':
        print('Просмотр остатков на складе')
        print('*'*80)
        if len(warehouse.equipment_in_warehouse()) == 0:
            print('Склад пустой!')
            continue #переходим на следующию итерацию цикла, for не отрабатывает
        for i, str in enumerate(warehouse.equipment_in_warehouse()):
            print(f'№{i + 1} {str}')
    elif in_str == '2':
        try:
            warehouse.add_equipment()
        except InputErrorDate as err:
            print(err)
    elif in_str == '3':
        # это просто пример на скорую руку, по хорошему можно реализовать поиск - вид техники(принтер/сканер/копир) + модель, но тут реализован поиск просто по модели, не успеваю
        model_ = input('введите название модели: ')
        quantity_ = input('Введите количество перемещаемой техники: ')
        try:
            if not quantity_.isdigit():
                raise InputErrorDate('Введенное Вами количество не являеться числом!')
            else:
                quantity_ = int(quantity_)
            warehouse.remove_equipment(model_, quantity_)
        except InputErrorDate as err:
            print(err)
