"""
Колесников Павел.
HW-8 от 25.01.2024
Игра Города
"""
from cities import cities_list

print('''****************************** ИГРА ГОРОДА ******************************
Для выхода напишите "стоп".
Или програйте...\n\n''')

city_set = set()  # Пустое множество.
for el_cities_list in cities_list:  # 
    city_set.add(el_cities_list["name"].lower())  # Добавляем все города по тегу 'name' в множество.
for city in list(city_set):  # Переводим множество в список, для проверки ниже.
    if city[-1] == 'ь' or city[-1] == 'ы' or city[-1] == 'ё' or city[-1] == 'й':  # Проверка в множестве "кривых" городов по последней букве элемента.
        city_set.remove(city)  # Удаляем их.

print(city_set)  # Проверочка.

used_city = []  # рабочий список для сравнения ответов.
game = True  # Переменная для управления основным циклом while.

while game:  # Пока переменная Thue цикл продолжается.
    count = 0
    user_input = input('Введите город: ').lower()  # приводим input к нижнему регистру для последующей проверки.
    if user_input.lower() == 'стоп':  # Проверка на пользовательский ввод "стоп" остановка игры.
        print('Джон Конор сдался... Машины победили...')
        game = False  # Останавливаем основной цикл while.
        break
    else:
        if not (user_input in city_set):  # Если города из input нет в множестве городов.
            print('Города не сущетвует или уже использовался. Машины победили...')
            game = False  # Останавливаем основной цикл while.
            break
        else:
            city_set.discard(user_input)  # Если город есть в множестве городов, то удаляем его из него.
            if count == 0:
                for city in city_set:
                    if city[0] == user_input[-1]:  # Проверка на первую и последнюю буквы.
                        print(f'ПК: {city.capitalize()}\n')  # Выводим вариант компьютера с большой буквы.
                        used_city.append(city)  # Добавляем в рабочий список город компьютера.
                        city_set.discard(city)  # Удаляем вариант компьютера из множества городов.
                        count += 1
                        break 
            elif count > 0 and used_city[0][-1] != user_input[0]:  # Проверка на первую и последнюю букву города из input и из рабочего списка.
                print(f'Город {user_input.capitalize()} начинается не на "{used_city[0][-1].capitalize()}"... Машины победили... ')
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
                print('Победа')
                game = False  # Останавливаем основной цикл while
                break








