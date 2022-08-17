class Date:
    month_dict = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'майя', 6: 'июнья', 7: 'июлья',
                  8: 'августа', 9: 'сентябрья', 10: 'октябрья', 11: 'ноябрья', 12: 'декабрья',}

    def __init__(self, _date):
        self._day = _date[0]
        self._month = _date[1]
        self._year = _date[2]

    @classmethod
    def set_date(cls, _date):
        date_list = _date.split('-')
        if not date_list[0].isdigit():
            raise NotCorectDateEx('День должен быть числом', None, date_list[0])
        if not date_list[1].isdigit():
            raise NotCorectDateEx('Месяц должен быть числом', None, date_list[1])
        if not date_list[2].isdigit():
            raise NotCorectDateEx('Год должен быть числом', None, date_list[2])
        return cls([int(i) for i in date_list])

    @staticmethod
    def get_date(obj, month_str = False):
        if 1 < obj._day > 31:
            raise NotCorectDateEx('Не корректно введен день месяца!', ' от 1 до 31 ', obj._day)
        if 1 < obj._month > 12:
            raise NotCorectDateEx('Не корректно введен месяц!', ' от 1 до 12 ', obj._month)
        if 1900 < obj._year > 2222:
            raise NotCorectDateEx('Не корректно введен год!', ' от 1900 до 2222 ', obj._day)
        if month_str:
            tmp_str = f'0{obj._day}:' if obj._day < 10 else f'{obj._day}:'
            tmp_str += f'0{obj._month}:{obj._year}' if obj._month < 10 else f'{obj._month}:{obj._year}'
        else:
            tmp_str = f'0{obj._day} ' if obj._day < 10 else f'{obj._day} '
            tmp_str += f'{obj.month_dict[obj._month]} {obj._year} года'
        return f'Введеная Вами дата: {tmp_str}'

class NotCorectDateEx(Exception):
    def __init__(self, _promt, _range, _inp):
        self._promt = _promt
        self._range = _range
        self._inp = _inp

    def __str__(self):
        tmp_str = f'Ошибка! - {self._promt}, введенное Вами значение - {self._inp}'
        return tmp_str  if self._range is None else tmp_str + ', допускаеться - ' + self._range
try:
    my_date = Date.set_date(input('Введите дату в формате "день-месяц-год": '))
    print(Date.get_date(my_date))
    print(Date.get_date(my_date, True))
except NotCorectDateEx as err:
    print(err)