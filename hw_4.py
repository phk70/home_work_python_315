"""
Колесников Павел.
HW-4 от 19.12.2023
Проверка телефона и пароля
"""

# Для проверки:
# +77053183958
# +77773183958
# 87773183958
# +(777)73183958
# +7(777)-731-83-58
# +7(777) 731 83 58

number = input('Номер телефона: ')
LEN_NUMBER = 11
bad_number = ''

# Очищаем написанный номер от лишнего кроме цифр
work_number = number.replace(' ','').replace('-','').replace('+','').replace('(','').replace(')','').lstrip().rstrip()

# Проверка наличия только цифр
if not work_number.isdigit():
    bad_number += f'-Номер содержит не допустимые символы\n'

# Проверка длины телефона
if len(work_number) != LEN_NUMBER:
    bad_number += f'-В номере недопустимое количество символов\n'

# Проверка первого символа
if not '7' <= work_number[0] <= '8':
    bad_number += f'-Номер начинается на не допустимую цифру\n'

# Итого выводим причины ошибок или подтверждаем номер
if bad_number:
    print(f'Ваш номер не прошел проверку по следующим причинам:\n{bad_number}')

else:
    print(f'Номер +7 {work_number[1:4]} {work_number[4:7]} '
    f'{work_number[7:9]} {work_number[9:]} прошел проверку')

# ПРОВЕРКА ПАРОЛЯ
password = input('Введите пароль: ')
LEN_PASWORD = 7
special_character = '!@#$%^&*()_+№;:?-=\/<>`~'
bad_password = ''

# Проверка длины пароля
if not len(password) > LEN_PASWORD:
    bad_password += f'-Пароль менее 7 символов\n'
    
# Проверка наличия пробелов
if password.count(' ') > 0:
    bad_password += f'-Пароль содержит пробелы\n'
    
# Проверка наличия спецсимволов
if set(special_character).isdisjoint(password):
    bad_password += f'-Пароль не содержит хотя бы 1 спецсимвол\n'

# Проверка наличия строчных букв
if sum(map(str.islower, password)) == 0:
    bad_password += f'-Пароль не содержит строчных букв\n'

# Проверка наличия заглавных букв
if sum(map(str.isupper, password)) == 0:
    bad_password += f'-Пароль не содержит заглавных букв\n'

# Итого выводим причины ошибок или подтверждаем пароль 
if bad_password:
    print(f'Введен не корректный формат пароля:\n{bad_password}')

else:
    print('Пароль принят')
    
    




