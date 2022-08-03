my_dict = {}

with open("text_6.txt", 'r', encoding='utf-8') as my_f:
    my_list = my_f.readlines()

for line in my_list:
    key, value = line.split(':')
    for x, y in ('(л)', ''), ('(пр)', ''), ('(лаб)', ''), ('-', ''):
        value = value.replace(x, y)
    my_dict.update({key: sum([int(i) for i in value.strip().split(' ') if i != ''])})

print(my_dict)
