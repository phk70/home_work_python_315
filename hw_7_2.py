"""
Колесников Павел.
HW-7-2 от 12.01.2024
Валидность телефонного номера
"""
# Номера для проверки: +77053183958;+77773183958;87773183958;+(777)73183958;+7(777)-731-83-58;+7(777) 731 83 58;+7(913)111-82-23 

input_numbers = input('Введите 11-ти значный номер телефона: ').split(';')
for number in input_numbers:
    clear_number = number.replace(' ','').replace('-','').replace('+','').replace('(','').replace(')','')
    if len(clear_number) > 11:
        raise ValueError(f'Номер {number} содержит больше 11 знаков.')
    elif len(clear_number) < 11:
        raise ValueError(f'Номер {number} содержит меньше 11 знаков.')
    elif not clear_number.isdigit():
        raise ValueError(f'Номер {number} содержит не только числа.')
    elif not '7' <= clear_number[0] <= '8':
        raise ValueError(f'Номер {number} начинается не с той цифры.')
    
    else:
        print(f'номер {number} прошел валидацию.')
print(f'Конец')













