nmb = int(input('Введите целое положительное число: '))
max_c = 0

while nmb != 0:
    if(nmb % 10 > max_c):
        max_c = nmb % 10
    nmb //= 10

print(f'Самая большая цифра в веденном числе - {max_c}')
