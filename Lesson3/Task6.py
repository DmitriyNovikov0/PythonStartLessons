def int_func(in_word):
    return in_word.capitalize()

def my_func(in_str):
    tmp_list = in_str.split(' ')
    return ' '.join( map(int_func, tmp_list))

print( my_func('lorem ipsum is simply dummy text of the printing and typesetting industry') )