from sys import argv

if len(argv) != 4:
    print('При запуске скрипта необходимо передать через пробел "выработка в часах", "ставка в час" и "премию"') #эпистолярный жанр у меня не развит пишу по дервенски
    exit(0)

_, w_hours, hourly_rate, premium = argv
try:
    print(f'Заработная плата составит: {int(w_hours) * int(hourly_rate) + int(premium)}')
except ValueError:
    print('Параметры должны быть числа')