inp_s =  int(input('Введите количество секунд: '))
h = inp_s // 3600
inp_s = inp_s % 3600 # берем остаток от деления inp_s на 3600
m = inp_s // 60
s = inp_s % 60

print('%02d:%02d:%02d' % (h, m, s))
