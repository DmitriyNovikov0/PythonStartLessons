s_nmb = input('Введите число: ')
# не правильно это без try catch делать, но мы пока не знаем об исключениях :)))))
print(f'{s_nmb} + {s_nmb + s_nmb} + {s_nmb + s_nmb + s_nmb} = {int(s_nmb) + int(s_nmb + s_nmb) + int(s_nmb + s_nmb + s_nmb)}')