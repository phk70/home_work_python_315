"""
Колесников Павел.
HW-15 от 27.02.2024
Ver. 2.0 от 05.03.2024
Классы для работы в стиле ООП
"""
import csv
import json
from pprint import pprint
from typing import List, Dict, Any

'''
Каждый класс должен обладать методами для
чтения, записи и дополнения данных в файлы соответствующего формата.

Класс CsvFileHandler

1. read_file(filepath, as_dict=False) : Метод для чтения данных из CSV файла. По
умолчанию данные должны возвращаться в виде списка списков, но при установке
флага as_dict в True , данные должны возвращаться в виде списка словарей.
Должен быть реализован как метод экземпляра.

2. write_file(filepath, data, as_dict=False) : Метод для записи данных в CSV файл.
По умолчанию метод должен записывать данные в виде списка списков, но при
установке флага as_dict в True , данные должны записываться в виде списка
словарей. Должен быть реализован как метод экземпляра.

3. append_file(filepath, data, as_dict=False) : Метод для дописывания данных в CSV
файл. Флаг as_dict работает аналогично как в методе write_file . Должен быть
реализован как метод экземпляра.
'''

class CsvFileHandler:
    """
    Класс для работы с CSV файлами
    """

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.data = None

    def read_file(self, as_dict: bool = False) -> List|Dict:
        """
        Открывает файл для чтения
        :param as_dict: Флаг варианта чтения список словарей / список списков
        """
        with open(self.filepath, 'r', encoding='windows-1251', newline='') as file:
            if as_dict:
                return [dict(row) for row in csv.DictReader(file)]
            else:
                return [row for row in csv.reader(file)]

    def write_file(self, data: List, as_dict: bool = False) -> None:
        """
        Перезаписывает файл *.CSV
        :param data: Данные для записи
        :param as_dict: Флаг варианта записи список словарей / список списков
        """
        with (open(self.filepath, 'w', newline='') as file):
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            if as_dict:
                writer.writeheader()
                writer.writerows(data)

    def append_file(self, data: List, as_dict: bool = False) -> None:
        """
        Дозаписывает данные в файл *.CSV
        :param data: Данные для дозаписи
        :param as_dict: Флаг варианта записи список словарей / список списков
        """
        with open(self.filepath, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            if as_dict:
                writer.writerows(data)
            else:
                for row in data:
                    writer.writerow(row)


'''
Класс JsonFileHandler

1. read_file(filepath, as_dict=False) : Метод для чтения данных из JSON файла. Флаг
as_dict работает аналогично как в классе CsvFileHandler . Должен быть реализован
как метод экземпляра.

2. write_file(filepath, data, as_dict=False) : Метод для записи данных в JSON файл.
Флаг as_dict работает аналогично как в классе CsvFileHandler . Должен быть
реализован как метод экземпляра.

3. append_file(filepath, data) : Метод для дописывания данных в JSON файл. При
попытке вызова этого метода должно возникать исключение TypeError с сообщением,
что данный тип файла не поддерживает операцию дописывания. Должен быть
реализован как метод экземпляра.
'''

class JsonFileHandler:
    """
    Класс для работы с JSON файлами
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def read_file(self, as_dict: bool = False):
        """
        Открывает файл для чтения
        :param as_dict: Флаг варианта чтения список словарей / список списков
        """
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            if as_dict:
                return data
            else:
                return [list(item.values()) for item in data]

        # with open(self.filepath, 'r', encoding='UTF-8') as file:
        #     if as_dict:
        #         return json.load(file)
        #     else:
        #         return json.load(file)

    def write_file(self, data: List|Dict, as_dict: bool = False):
        """
        Перезаписывает файл *.JSON
        :param data: Данные для записи
        :param as_dict: Флаг варианта записи список словарей / список списков
        """
        with open(self.filepath, 'w', encoding='UTF-8') as file:
            if as_dict:
                json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                json.dump(data, file, ensure_ascii=False, indent=4)

    def append_file(self, data: List|Dict):
        raise ValueError('Данный тип файла не поддерживает дозапись')

'''
Класс TxtFileHandler

1. read_file(filepath) : Метод для чтения данных из TXT файла. Должен быть
реализован как метод экземпляра.

2. write_file(filepath, data) : Метод для записи данных в TXT файл. Должен быть
реализован как метод экземпляра.

3. append_file(filepath, data) : Метод для дописывания данных в TXT файл. Должен
быть реализован как метод экземпляра.
'''

class TxtFileHandler:
    """
    Класс для работы с TXT файлами
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def read_file(self):
        """
        Открывает файл для чтения
        """
        with open(self.filepath, 'r', encoding='windows-1251') as file:
            return file.readlines()

    def write_file(self, data: Any):
        """
        Перезаписывает данные в файле *.TXT
        :param data: Данные для записи
        """
        with open(self.filepath, 'w') as file:
            file.write(str(data) + '\n')

    def append_file(self, data: Any):
        """
        Дозаписывает данные в файл *.TXT
        :param data: Данные для дозаписи
        """
        with open(self.filepath, 'a') as file:
            file.write(str(data) + '\n')


#                                       П  Р  О  В  Е  Р  К  И

print('************************************** ПРОВЕРКА CSV **************************************')
csv_handler = CsvFileHandler('data.csv')
csv_data = [
    {'name': 'Pavel', 'surname': 'Kolesnikov', 'age': 37},
    {'name': 'Tanya', 'surname': 'Kolesnikova', 'age': 30},
]

# csv_handler.write_file(csv_data, True)
# csv_handler.append_file(csv_data, False)
print('Список Словарей')
pprint(csv_handler.read_file(True), sort_dicts=False)
print('Список Списков')
pprint(csv_handler.read_file(False), sort_dicts=False)

print('\n************************************** ПРОВЕРКА JSON **************************************')
json_handler = JsonFileHandler('data.json')
json_data = [{'name': 'Pavel', 'age': 37}, {'name': 'Tanya', 'age': 30}]
# json_handler.write_file(json_data, False)
# json_handler.append_file(json_data)
print('Список Списков')
pprint(json_handler.read_file(False), sort_dicts=False)
print('Список Словарей')
pprint(json_handler.read_file(True), sort_dicts=False)

print('\n************************************** ПРОВЕРКА TXT **************************************')
txt_handler = TxtFileHandler('data.txt')
# txt_handler.write_file('Перезапись txt')
# txt_handler.append_file(123)
print(txt_handler.read_file())
