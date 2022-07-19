from functools import reduce

def my_mult(prev_el, el):
    return prev_el * el
#я тут не понял условия до 1000 включительно? если так то в rande верхняя граница 1001, если до 1000 то верхняя граница 1000 :)
print(reduce(my_mult, [i for i in range(100, 1001) if i % 2 == 0]))