"""
Колесников Павел.
HW-7 от 12.01.2024
Валидация списка на INT
"""
data_lst = ['1', '2', '3', '4d', 5]
new_data_lst = []
count = 1
for data in data_lst:
    try:
        data = int(data)
        new_data_lst.append(data)
        count += 1
    except TypeError:
        print(f'данные {count}-го числа не валидны. {data} не число.')    
        continue
    except ValueError:
        print(f'данные {count}-го числа не валидны. {data} не число.')
        continue
            
print(f'\nВалидный список {new_data_lst}')
    
