my_str = ' '
out_f = open("out_file.txt", "w")

while my_str != '':
    my_str = input('Введите строку(для выхода нажмите Enter): ')
    #out_f.write(my_str + '/n') либо через write либо через print
    print(my_str, file = out_f)

out_f.close()