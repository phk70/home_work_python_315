"""
Колесников Павел.
HW-12 от 13.02.2024
Однострочники. Генераторы. Сортировка. Фильтр.
"""
from pprint import pprint
from typing import List, Dict, Union, Set, Callable, Any
from marvel import full_dict

marvel_list: List = [film for film in full_dict.values()]

print('********************************** 1. ИМПОРТ FULL-DICT *****************************************************\n')
""" Сделайте импорт full_dict из документа Marvel.py """

print('Сделано')

print('\n********************************** 2. ВВОД ПОЛЬЗОВАТЕЛЯ **************************************************\n')
"""
Напишите пользовательский ввод цифр через пробел, разбейте его на список, и примените к каждому элементу списка 
int используя map , но только в том случае, если этот элемент списка число, иначезамените его на None.
"""

user_enter_number: List[str] = input(f'Введите цифры от 0 до {len(full_dict)-1} через пробел: ').split(' ')
user_number_list_id: List[int | None] = list(map(lambda integer: int(integer) if integer.isdigit()
    else None, user_enter_number))
print(user_number_list_id)

print('\n********************************** 3. FILTER ФИЛЬМОВ ПО ID = ВВОДУ ПОЛЬЗОВАТЕЛЯ **************************\n')
"""
Используйте filter и получите аналогичный по структуре словарь, который будет содержать исходные id
и остальные ключи, но только тех фильмов, id которых есть в полученном списке в п.2.
"""

films_id: Dict[int, Dict[str, Union[str, int]]] = {key: value for key, value in full_dict.items()
  if key in user_number_list_id}
pprint(films_id, sort_dicts=False)

print('\n********************************** 4. SET COMPREHENSION ПО КЛЮЧУ DIRECTOR ********************************\n')
"""
Составьте set comprehension (генератор множества) собрав множество содержимого ключа director
словаря дата-сета.
"""

set_director: Set[str] = {value['director'] for key, value in full_dict.items()}
pprint(set_director, sort_dicts=False)

print('\n********************************** 5. DICT COMPREHENSION + YEAR --> "YEAR" *******************************\n')
"""
Составьте dict comprehension (генератор словаря) сделав копию исходного словаря full_dict, при этом
применим в к каждому 'year' значению, функцию str.
"""

full_dict_copy: Dict[int, Dict[str, Union[str, None]]] = dict({key: {key: str(value) if key == 'year' else value
    for key, value in value.items()} for key, value in full_dict.items()})
pprint(full_dict_copy, sort_dicts=False)

print('\n********************************** 6. FILTER ФИЛЬМОВ НА "Ч" **********************************************\n')
"""
Используйте filter и получите аналогичный по структуре словарь, который будет содержать исходные id
и остальные ключи, но только тех фильмов, которые начинаются на букву Ч.
"""

films_ch: Dict[int, Dict[str, Union[str, int, None]]] = {key: value for key, value in full_dict.items()
    if isinstance(value['title'], str) and value['title'].startswith('Ч')}
pprint(films_ch, sort_dicts=False)

print('\n********************************** 7. СОРТИРОВКА FULL_DICT ПО DIRECTOR ***********************************\n')
"""
Опционально: Сделайте сортировку словаря full_dict по одному (любому) параметру, с использованием
lambda на выходе аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы
делаете сортировку!
"""

sort_dict: Dict[int, Dict[str, Union[str, int, None]]] = dict(sorted(full_dict.items(), key=lambda x: x[1]['director']
    if isinstance(x[1]['director'], str) else 'я'))
pprint(sort_dict, sort_dicts=False)

print('\n********************************** 8. СОРТИРОВКА FULL_DICT ПО 2 ПАРАМЕТРАМ YAER + DIRECTOR ***************\n')
"""
Опционально: сделайте сортировку словаря full_dict по двум (любом) параметрам, с использованием
lambda на выходе аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы
делаете сортировку!
"""

sort_dict_two_param: Dict[int, Dict[str, Union[str,int,None]]] = dict(filter(lambda x: isinstance(x[1]['year'], int)
    and isinstance(x[1]['director'], str), full_dict.items()))
pprint(sort_dict_two_param, sort_dicts=False)

print("""\n******************************** 9. СОЗДАНИЕ FULL_DICT + СОРТИРОВКА FULL_DICT С ИСП. SORTED **************
отсортировано по 'director'
фильтр по 'year'\n""")
"""
Опционально: напишите однострочник, в котором мы получаем аналогичный по структуре full_dict но
отфильтрованный через filter и с использованием в этой же строке sorted.
"""

full_dict_sort_filter: Dict[int, Dict[str, Any]] = dict(sorted(filter(lambda x: x[1]['year'] ==
    2017, full_dict.items()), key=lambda x: x[1]['director']))
pprint(full_dict_sort_filter, sort_dicts=False)

print('\n********************************** 10. Аннотация типов и MYPY ********************************************\n')
""" 
Опционально: напишите аннотацию типов для переменных, в которых будет результат и пройдите проверку
mypy (оставьте сообщение в комментариях в коде об успешной проверке. Я всё читаю!)
"""
# Итог проверки MYPY:
# PS D:\PYTHON-315\Python\HW_PY> mypy .\hw_py_30_1.py
# Success: no issues found in 1 source file
# PS D:\PYTHON-315\Python\HW_PY>


print('\n********************************** 11. КРАСИВЫЙ PRINT*****************************************************\n')
"""
Сделайте красивый принт результатов pprint с подписью, какое задание и где выполнено (помните, что
у него надо выключить сортировку, иначе он сортирует словарь еще раз). 
"""
print('Сделано в теле работы')


""" 
Критерии проверки:
1. Все условия выполнены (опциональные - по желанию)
2. Хороший нейминг переменных
3. PEP-8
4. Вся работа в ОДНОМ ФАЙЛЕ
5. (сдайте просто ОДИН PY файл с решением, пожалуйста не загружайте дата-сет, и тем более архив... и тем
более архив с виртуальным окружением проекта!)
6. Используйте импорт именно в этом ф
"""