import json

average_profit = 0
my_dict = {}
data = []
with open("text_7.txt", 'r', encoding='utf-8') as my_f:
    my_list = my_f.readlines()

for firm in my_list:
   tmp_list = firm.strip().split(' ')
   tmp_profit = int(tmp_list[2]) - int(tmp_list[3])
   my_dict.update({tmp_list[0]: tmp_profit})
   if tmp_profit > 0:
       average_profit += tmp_profit

data.append(my_dict)
data.append({'average_profit': average_profit / len(my_list)})

#вот с кодировкой фигня получилась....
with open("text_77.json", "w", encoding='utf-8') as write_f:
    json.dump(data, write_f)
