"""
Колесников Павел.
HW-6 от 26.12.2023
Генератор пословиц
"""
import random

proverbs = [
    "Ум хорошо, а два лучше.",
    "Ум — горячая штука.",
    "Ум всё голова.",
    "Умом Россию не понять.",
    "Ум бережет, а глупость губит.",
    "Ум в голову приходит.",
    "Ум от ума не горит.",
    "Умом нагружен, а волосы развеваются.",
    "Умом обдумал, а ногами пошел.",
    "Ум — сокровище, не пропадет без него и копье на ветру.",
    "Ум — грех, а бес — мера.",
    "Ум есть богатство.",
    "Ум роднит народы.",
    "Ум краток, да забот — бездна.",
    "Ум не камень, взял и положил.",
    "Ум не велит, а наставляет.",
    "Ум с мерой, а глупость без меры.",
    "Ум — сокол, глаз его — телескоп.",
    "Ум — не конская морда, не разобьешь.",
    "Ум — семь пядей во лбу.",
    "Ум — не барсук, в нору не залезет.",
    "Ум в голове, а не на ветру.",
    "Ум греет душу, а глупость терпение.",
    "Ум служит человеку, а глупость — хозяином.",
    "Ум мил, да безумству хозяин.",
    "Ум в труде, да наслаждение в праздности.",
    "Ум глаза исправляет.",
    "Ум человека не обманешь.",
    "Ум на подобии огня — без сна не останешься.",
    "Ум к уму приходит.",
    "Ум с пользой тратит время.",
    "Ум желание творит.",
    "Ум общего дела дело.",
    "Ум — друг, а воля — враг.",
    "Ум — бесценное сокровище.",
    "Ум тонок, да разум невелик.",
    "Ум — враг бедности.",
    "Ум — теремок, да не на прокол.",
    "Ум силен, да не камень.",
    "Ум рассудит, что сердце не посоветует.",
    "Ум — подкова, а топор — ось.",
    "Ум легче камня, да весомей золота.",
    "Ум не вешать на гроздья.",
    "Ум — не мешок, на плечи не вешай.",
    "Ум — лучшая победа.",
    "Ум — в суде велик, а в деле своем мал.",
    "Ум голове краса.",
    "Ум — сокровище, а глупость — нищета.",
    "Ум человека — огонь, а глаза — масло.",
    "Ум — путь, а дорога — конец.",
    "Ум стоит денег.",
    "Ум от смеха бьет в ладоши.",
    "Ум — коза, к барскому плечу привыкает.",
    "Ум — лезвие, а лень — ржавчина.",
    "Ум на вершине — мир в руках.",
]

variants = [
    'кот',
    'шеф',
    'мозг',
    'лес',
    'фолк',
    'код',
    'рот',
    'мёд',
    'лук',
    'лес',
    'год',
    'час',
    'друг',
    'жена',
    'муж',
    'айфон',
    'работа',
]

answer = int(input('Сколько пословиц хотите? '))
result_list = []
count = 0
result_count = 0

if answer <= len(proverbs):
    while count < answer and len(proverbs) != 0:
        random_proverbs = random.choice(proverbs)  #Вытаскиваем рандомную строку
        list_random_proverbs = random_proverbs.split()  #преобразуем в список с разделителем по пробелу
        index_proverbs = proverbs.index(random_proverbs)  #Получаем индекс найденной пословицы
        proverbs.pop(index_proverbs)  #Удаляем первоначальную пословицу
        random_variant = random.choice(variants)  #Вытаскиваем рандомную строку из вариантов замены
        list_random_proverbs[0] = random_variant  #Меняем первое слово Ум на рандомный вариант
        result_list.append(list_random_proverbs)  #МДобавляем в конец итогового списка
        count += 1
else:
    print(f'Вы ввели {answer}, но максимальное количество пословиц всего {len(proverbs)}\n'
    'Приносим свои извинения, и усердно работаем над наполнением контента.\n\n'
    'Но мы больше не знаем никаких пословиц...')


for item in result_list:  #Для каждого элемента получившегося списка
    result_count += 1  #Чисто для наглядности
    item = ' '.join(item)  #Преобразуем в строку
    print(f'{result_count}. {item.capitalize()}')  #И заглавную букву вместо вишенки.
    

