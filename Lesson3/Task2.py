def my_func(user_name, user_surname, user_year, user_city, user_email, user_phone):
    """
    функция выводит на экран информацию о пользователе
    :param user_name: имя
    :type user_name: str
    :param user_surname: фамилие
    :type user_surname: str
    :param user_year: год рождения
    :type user_year: str
    :param user_city: город
    :type user_city: str
    :param user_email: email
    :type user_email: str
    :param user_phone: телефон
    :type user_phone: str
    :return: ничего не возвращает
    """
    print(f'{user_surname} {user_name}, год рождения: {user_year}, проживает в городе: {user_city}, email: {user_email}, телефон: {user_phone}')

my_func(user_name = input('Введите имя: '), user_surname = input('Введите фамилия: '), user_year = input('Год рождения: '),
        user_city = input('город: '), user_email = input('email: '), user_phone = input('телефон: '))