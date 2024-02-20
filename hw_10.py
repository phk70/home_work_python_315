"""
Колесников Павел.
HW-10 от 07.02.2024
Рефакторинг игры "Города". Функции.
"""
"""
Присутствует функция подсчета побед, которая читает числа из count.json
При первом использовании необходимо раскомментировать в f(main) строки:
№ 143 create_count('count.json') для создания файла со счетом
№ 144 create_cities_set('cities.json') для создания файла с городами
После первого прогона комментируем обратно
"""
import json
import time
import locale
from datetime import datetime
from typing import List, Dict

from cities import cities_list

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # локализация РФ


def create_cities_set(name_file: [str]) -> None:
    """
Создает и записывает чистый список городов без плохих букв в '***.json'
    :param name_file: Имя файла в который записывается '***.json'
    """
    cities_set = {city['name'].title() for city in cities_list}
    # Сет уникальных букв из всего сета городов
    unique_letters_set = set(''.join(cities_set).lower())
    # Сет плохих букв
    bad_letters_set = set()
    # Проходим циклом по уникальным буквам, проверяем есть ли в сете городов город
    # Который начинается на эту букву.
    for letter in unique_letters_set:
        for city in cities_set:
            if city[0].lower() == letter:
                break
        else:
            # Если города на уникальную букву нет, то помещаем ее в множество плохих
            bad_letters_set.add(letter)
    # Удаляем города с плохими буквами в конце:
    for city in list(cities_set):
        if city[-1] in list(bad_letters_set):
            cities_set.remove(city)
            cities_set = list(cities_set)
    # Записываем в JSON
    with open(name_file, 'w', encoding='UTF-8') as file:
        json.dump(cities_set, file, ensure_ascii=False, indent=4)


def save_data_in_file(name: [str], name_file: [str]) -> None:
    """
Записывает созданный список/словарь в файл JSON
    :param name: Имя списка/словаря/кортежа, который записываем
    :param name_file: Имя файла в который записываем '***.json'
    """
    with open(name_file, 'w', encoding='UTF-8') as file:
        name = json.dump(name, file, ensure_ascii=False, indent=4)


def load_data_from_file(name: [str], name_file: [str]) -> List[str]:
    """
Загружает список/словарь из файла JSON
    :param name: Имя списка/словаря/кортежа, который загружаем
    :param name_file: Имя файла из которого загружаем '***.json'
    """
    with open(name_file, 'r', encoding='UTF-8') as file:
        name = json.load(file)
        return name


def create_count(name_file: [str]) -> None:
    """
Создает и записывает пустой счет в '***.json'
    :param name_file: Имя файла в который записывается счет
    """
    count_win = {
        'Победа компьютера': 0,
        'Победа пользователя': 0
    }
    with open(name_file, 'w', encoding='UTF-8') as file:
        count_win = json.dump(count_win, file, ensure_ascii=False, indent=4)


def up_count(name: [str], key: [int], point: int) -> int:
    """
Увеличивает значение счета статистики на заданное количество очков
    :param name: Имя словаря со статистикой
    :param key: Ключ словаря (ПК или Пользователь)
    :param point: Количество очков
    """
    name[key] += point
    return name[key]


def game_over() -> None:
    """
Просто заставка в конце
    :return: КОНЕЦ
    """
    time.sleep(2)
    print("\n" * 100)
    print('''  ****        ****       *****           ****        ****    ************    ****     ****''')
    time.sleep(0.1)
    print('''  ****      ****      ***********        ****        ****    ************    ****     ****''')
    time.sleep(0.1)
    print('''  ****    ****      ****       ****      ****        ****    ****            ****     ****''')
    time.sleep(0.1)
    print('''  ****  ****       ****         ****     ****        ****    ****            ****     ****''')
    time.sleep(0.1)
    print('''  ********        ****           ****    ****************    ************    ****     ****''')
    time.sleep(0.1)
    print('''  ********        ****           ****    ****************    ************    ****     ****''')
    time.sleep(0.1)
    print('''  ****  ****       ****         ****     ****        ****    ****            ****     ****''')
    time.sleep(0.1)
    print('''  ****    ****      ****       ****      ****        ****    ****            ****     ****''')
    time.sleep(0.1)
    print('''  ****      ****      ***********        ****        ****    ************    *****************''')
    time.sleep(0.1)
    print('''  ****        ****       *****           ****        ****    ************    *****************''')
    time.sleep(0.1)
    print('''                                                                                          ****''')
    time.sleep(0.1)
    print('''                                                                                          ****''')


def change_count(name_file: [str], name: [Dict[str, str]], key: [str], point: [int]) -> None:
    """
При изменении счета вызываются все ф-ии изменений + game over
    :param name_file: Имя файла json в ''
    :param name: Имя словаря в котором лежит счет без ''
    :param key: имя ключа ('Победа компьютера' или 'Победа пользователя')
    :param point: Количество очков для прибавления в статистике
    """
    load_data_from_file(name, name_file)
    up_count(name, key, point)
    save_data_in_file(name, name_file)
    game_over()


def main():
    # create_count('count.json')  # Комментируем после записи данных в файл
    # create_cities_set('cities.json')  # Комментируем после записи данных в файл

    # Загружаем города и счет из файлов

    cities_set = load_data_from_file('cities_set', 'cities.json')
    count_win = load_data_from_file('count_win', 'count.json')

    # Проверка количества раундов. Если сумма побед больше 5, то обнуляем счетчик
    # TODO: Но почему то 5 не работает, все делится на 2. Ставлю 8 и тогда норм считается до 5.
    if (count_win['Победа компьютера'] + count_win['Победа компьютера']) > 8:
        load_data_from_file(count_win, 'count.json')  # Достаем счет
        count_win['Победа компьютера'] = 0  # обнуляем счет
        count_win['Победа пользователя'] = 0  # обнуляем счет
        save_data_in_file(count_win, 'count.json')  # записываем нулевой счет в файл

    now_date = datetime.now()  # Текущая дата

    print(f'\t\n{now_date.strftime('%d %B %Y')}\n{now_date.strftime('%A').capitalize()}')  # Формат даты
    print('''
    *******************************************************************************************
    *******************************    И Г Р А   Г О Р О Д А    *******************************
    *******************************************************************************************''')

    print(f'Счет последних пяти игр:\nКомпьютер - {count_win['Победа компьютера']}\n'
          f'Игрок - {count_win['Победа пользователя']}\n\nДля выхода напишите "стоп".'
          f' Если вы ленивый, то можете набрать "й" или "q".\nИли просто програйте...\n')

    ii_city = None

    # Описываем игру
    while True:
        # ************************************** Ход игрока *********************************************
        # ***********************************************************************************************
        user_city = input('Введите город: ').strip().title()

        # Остановка игры
        if user_city.lower() == 'стоп' or user_city.lower() == 'q' or user_city.lower() == 'й':
            print('Джон Конор сдался... Машины победили...\U0001F480 \U0001F480 \U0001F480')
            change_count('count.json', count_win, "Победа компьютера", 1)
            break

        # Проверка наличия города в списке городов
        if user_city not in cities_set:
            print('Города нет в РФ или уже использовался. Машины опять победили...\U0001F480 \U0001F480 \U0001F480')
            change_count('count.json', count_win, "Победа компьютера", 1)
            break

        if ii_city:
            # Проверка последней буквы
            if user_city[0].lower() != ii_city[-1].lower():
                print(
                    f'Город {user_city.title()} начинается не на "{ii_city[-1].capitalize()}"... '
                    f'Машины снова победили...\U0001F480 \U0001F480 \U0001F480')
                change_count('count.json', count_win, "Победа компьютера", 1)
                break

        # Если проверку прошли, то удаляем город пользователя из списка городов
        cities_set.remove(user_city)

        # ************************************** Ход компьютера *****************************************
        # ***********************************************************************************************

        # Поиск города, соответствующего последней букве человеческого города
        last_user_letter = user_city[-1]
        # Перебираем города в сете
        for city in set(cities_set):
            # Если первая буква города совпадает с последней буквой человеческого города
            if city[0].lower() == last_user_letter:
                print(f'ПК:{city.title()}\n******************************************************'
                      f'*************')
                # Запоминаем город
                ii_city = city
                # И удаляем его из общего списка городов
                cities_set.remove(city)
                break
        else:
            # Если нет подходящего города в списке городов - компьютер проиграл
            print('Победа \U0001F973 \U0001F973 \U0001F973')
            change_count('count.json', count_win, "Победа пользователя", 1)
            break


if __name__ == '__main__':
    main()
