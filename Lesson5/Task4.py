my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыри', 'Five': 'Пять'}
my_list = []

with open("text_4.txt", "r", encoding='utf-8') as my_f:
    for line in my_f:
        for key in my_dict.keys():
            line = line.replace(key, my_dict[key])
        my_list.append( line )

with open("text_4_out.txt", 'w', encoding='utf-8') as out_f:
    out_f.writelines(my_list)
