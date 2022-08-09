proceeds = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))

if(proceeds > costs):
    print(f'фирма прибыльная, рентабильность составляет {proceeds / costs :.2f}\n')
else:
    print('фирма убытачная\n')

c_person = int(input('Введите количество сотрудников: '))
print(f'прибыль в расчете на одного сотрудника {(proceeds - costs) / c_person:.2f}')