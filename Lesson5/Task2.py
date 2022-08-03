with open("text_2.txt", "r", encoding='utf-8') as my_f:
    my_list = my_f.readlines()

print(f'В файле {my_f.name} содержиться {len(my_list)} строк')
for i in range(len(my_list)):
    print(f'в строке №{i + 1} {str(len(my_list[i].split()))} слов')