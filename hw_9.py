"""
Колесников Павел.
HW-9 от 27.01.2024
Игра Города. With open
"""
from cities import cities_list  # Он тут как бы уже и не нужен, но пусть полежит.
import json
import time
from _datetime import datetime

now_date = datetime.now()
print(f'{now_date.strftime('%d-%b-%Y')}')
print('''****************************** ИГРА ГОРОДА ******************************
Для выхода напишите "стоп".
Или програйте...\n\n''')

# 16-37 КОММЕНИРУЕМ ДЛЯ ПРОВЕРКИ ЧТЕНИЯ ИЗ count.json
#
# city_set = {city['name'].lower() for city in cities_list}  # Наполняем множество городами
# # Находим уникальные буквы в городах
# unique_letter_to_city_set = set(''.join(city_set))
# print(unique_letter_to_city_set)
# # Создаем множество с буквами, на которые не начинается ни один город
# bad_letter_set = set()
# for letter in unique_letter_to_city_set:
#     for city in city_set:
#         if city[0] == letter:
#             break
#     else:
#         bad_letter_set.add(letter)
#
# # Удаляем города, которые начинаются на плохие буквы
# for city in list(city_set):
#     if city[-1] in list(bad_letter_set):
#         city_set.remove(city)
#
# city_set = list(city_set)  # Переводим множество в список.
# # Записываем данные из списка city_set в json файл
# with open('new_city_set.json', 'w', encoding='UTF-8') as file:
#     json.dump(city_set, file, ensure_ascii=False, indent=4)

with open('new_city_set.json', 'r', encoding='UTF-8') as file:  # Читаем данные из файла new_city_set.json
    city_set = json.load(file)  # Выгружаем их обратно в список.
city_set=set(city_set)  # Преводим полученный из json список обратно в множество  для дальнейшей работы.

# Создаем словарь для подведения итогов. ПОТОМ КОММЕНТИМ С 44 по 50
# count_win = {
#     'Победа компьютера': 0,
#     'Победа пользователя': 0
# }
# # Записываем в него нулевые значения в count.json
# with open('count.json', 'w', encoding='UTF-8') as file:
#     json.dump(count_win, file, ensure_ascii=False, indent=4)
#Читаем словарь из файла count.json и записываем его снова в словарь
with open('count.json', encoding='UTF-8') as file:
    count_win = json.load(file)
if int(count_win['Победа компьютера'] + count_win['Победа компьютера']) > 10:  # Я не понимаю почему 10, но так работает)))
    with open('count.json', encoding='UTF-8') as file:  # открываем файл
        count_win = json.load(file)  # достаем словарь со счетом
    count_win['Победа компьютера'] = 0  # меняем счет
    count_win['Победа пользователя'] = 0
    with open('count.json', 'w', encoding='UTF-8') as file:
        json.dump(count_win, file, ensure_ascii=False, indent=4)

print(f'Счет последних пяти игр\n{count_win}\n', sep='')

# ДАЛЬШЕ ВСЕ ПО СТАРОЙ СХЕМЕ ИЗ HW-26, только добавлено чтение, выгрузка, исправление и обратная загрузка
# словаря count_win в зависимости от результатов игры (65-69, 76-80, 97-101, 115-119)

used_city = []  # рабочий список для сравнения ответов.
game = True  # Переменная для управления основным циклом while.

while game:  # Пока переменная Thue цикл продолжается.
    count = 0
    user_input = input('Введите город: ').lower()  # приводим input к нижнему регистру для последующей проверки.
    if user_input.lower() == 'стоп':  # Проверка на пользовательский ввод "стоп" остановка игры.
        time.sleep(1)
        print('Джон Конор сдался... Машины победили...')
        with open('count.json', encoding='UTF-8') as file:  # открываем файл
            count_win = json.load(file)  # достаем словарь со счетом
        count_win['Победа компьютера'] += 1  # меняем счет
        with open('count.json', 'w', encoding='UTF-8') as file:
            json.dump(count_win, file, ensure_ascii=False, indent=4)  # записываем обратнов json
        game = False  # Останавливаем основной цикл while.
        break
    else:
        if not (user_input in city_set):  # Если города из input нет в множестве городов.
            time.sleep(1)
            print('Города не сущетвует или уже использовался. Машины победили...')
            with open('count.json', encoding='UTF-8') as file:  # открываем файл
                count_win = json.load(file)  # достаем словарь со счетом
            count_win['Победа компьютера'] += 1  # меняем счет
            with open('count.json', 'w', encoding='UTF-8') as file:
                json.dump(count_win, file, ensure_ascii=False, indent=4)  # записываем обратнов json
            game = False  # Останавливаем основной цикл while.
            break
        else:
            city_set.discard(user_input)  # Если город есть в множестве городов, то удаляем его из него.
            if count == 0:
                for city in city_set:
                    if city[0] == user_input[-1]:  # Проверка на первую и последнюю буквы.
                        time.sleep(1)
                        print(f'ПК: {city.title()}\n')  # Выводим вариант компьютера с большой буквы.
                        used_city.append(city)  # Добавляем в рабочий список город компьютера.
                        city_set.discard(city)  # Удаляем вариант компьютера из множества городов.
                        count += 1
                        break
            elif count > 0 and used_city[0][-1] != user_input[0]:  # Проверка на первую и последнюю букву города из input и из рабочего списка.
                time.sleep(1)
                print(f'Город {user_input.title()} начинается не на "{used_city[0][-1].capitalize()}"... Машины победили... ')
                with open('count.json', encoding='UTF-8') as file:  # открываем файл
                    count_win = json.load(file)  # достаем словарь со счетом
                count_win['Победа компьютера'] += 1  # меняем счет
                with open('count.json', 'w', encoding='UTF-8') as file:
                    json.dump(count_win, file, ensure_ascii=False, indent=4)  # записываем обратнов json
                game = False  # Останавливаем основной цикл while.
                break
            elif count > 0 and used_city[0][-1] == user_input[0]:  # Проверка на первую и последнюю букву города из input и первого и единственного горда из рабочего списка.
                used_city.clear()  # Если совпадает, то очищаем рабочий список.
                for city in city_set:
                    if city[0] == user_input[-1]:
                        print(city)
                        used_city.insert(0,city)  # Меняем единственный элемент рабочего списка на на выбранный город.
                        city_set.discard(city)  # И так же удаляем этот город из множества городов.
                        break
            else:  # Если ничего из выше изложенного не случилось, значит мы победили.
                time.sleep(1)
                print('Победа')
                with open('count.json', encoding='UTF-8') as file:  # открываем файл
                    count_win = json.load(file)  # достаем словарь со счетом
                count_win['Победа пользователя'] += 1  # меняем счет
                with open('count.json', 'w', encoding='UTF-8') as file:
                    json.dump(count_win, file, ensure_ascii=False, indent=4)  # записываем обратнов json
                game = False  # Останавливаем основной цикл while
                break








