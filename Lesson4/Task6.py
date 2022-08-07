from itertools import count
from itertools import cycle
my_list = []

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
        my_list.append(el)

print('******* ')
с = 0
for el in cycle(my_list):
    if с > 20:
        break
    print(el)
    с += 1