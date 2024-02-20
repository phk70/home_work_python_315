"""
Колесников Павел.
HW-13 от 19.02.2024
Декораторы валидации пароля
"""
import csv
from typing import Callable

"""
Часть 1
Цель задания:
Написать программу для регистрации пользователей с использованием декоратора для проверки сложности пароля.

Инструкции:
1. Напишите функцию password_checker , которая будет являться декоратором. Декоратор должен проверять сложность 
пароля согласно следующим условиям:    
    Длина пароля должна быть не менее 8 символов.
    Пароль должен содержать хотя бы одну цифру.
    Пароль должен содержать хотя бы одну заглавную букву.
    Пароль должен содержать хотя бы одну строчную букву.
    Пароль должен содержать хотя бы один спецсимвол (например, !, @, #, $ и т.д.).
    
    Если пароль соответствует всем условиям, функция-декоратор должна вызвать оригинальную
    функцию. В противном случае, вернуть сообщение об ошибке.
2. Напишите функцию register_user , которая будет принимать пароль в качестве аргумента. Эта функция будет возвращать 
сообщение о успешной регистрации, если пароль прошел проверку, и сообщение об ошибке в противном случае.
3. Используйте декоратор @password_checker для функции register_user . При вызове функции register_user, декоратор 
должен автоматически проверить сложность пароля.
4. Напишите примеры использования декоратора для проверки сложности пароля:
    Вызовите функцию register_user с разными паролями, включая те, которые соответствуют
    всем условиям и те, которые не соответствуют хотя бы одному из условий.
    Выведите соответствующие сообщения об успешной регистрации или об ошибках.

Критерии проверки:
    Чистый код
    Хороший нейминг
    Аннотации типов (включая Typing )
    Программа должна проходить проверку mypy
    Протестируйте код с разными вариантами паролей, чтобы убедиться, что декоратор корректно обрабатывает
    различные ситуации.
"""

spec_char: str = '!@#$%^&*()_+=-<>'
numbers: str = '0123456789'
# TODO: Почему-то проверка isdigit() в декораторе ниже никак не хотела работать, поэтому сделал список цифр и цикл.


def password_checker(length: int, digit: int, uppercase: int, lowercase: int, special: int) -> Callable:
    """
Функция-декоратор принимает значения и проверяет по ним входящий пароль
    :param length: минимальная длина пароля
    :param digit: обязательное количество цифр
    :param uppercase: обязательное количество букв верхнего регистра
    :param lowercase: обязательное количество букв нижнего регистра
    :param special: обязательное количество специальных символов
    """
    def decorator(func: Callable) -> Callable:
        """
        Функция принимает ссылку на функцию и возвращает ссылку на функцию
        :param func: Callable
        """

        def wrapper(password: str) -> Callable:
            """
            Функция принимает аргументы и возввращает ссылку
            :param password: str
            """

            count_digit: int = 0
            for i in password:
                if i in numbers:
                    count_digit += 1

            count_uppercase: int = sum(1 for letter in str(password) if letter.isupper() == True)
            count_lowercase: int = sum(1 for letter in str(password) if letter.islower() == True)
            count_special: int = sum(1 for letter in str(password) if letter in spec_char)

            if (len(password)) <= length:
                raise ValueError(f'\nПароль {password} слишком короткий. Минимум {length} символов.')
            elif count_digit < digit:
                raise ValueError(f'\nПароль {password} не содержит минимум {digit} цифру.')
            elif count_uppercase < uppercase:
                raise ValueError(f'\nПароль {password} не содержит минимум {uppercase} символ верхнего регистра.')
            elif count_lowercase < lowercase:
                raise ValueError(f'\nПароль {password} не содержит минимум {lowercase} символ нижнего регистра.')
            elif count_special < special:
                raise ValueError(f'\nПароль {password} не содержит минимум {special} спец знак.')

            return f'Все ок, пароль: ' + func(password)
        return wrapper
    return decorator


@password_checker(8, 1, 1, 1, 1)
def register_user(password: str) -> str:
    """
   Функция принимает один аргумент и возвращает строку для проверки
   :param user_password:
   """
    return password

# ПРОВЕРКИ
# Тестирование успешного случая
try:
    register_user("Rff2$345$$$")
    print('Пароль успешен')
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование Верхнего регистра
try:
    register_user("23sf345f43f")
    print('Пароль успешен')
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование цифр
try:
    register_user("JRRRgggff#f")
    print('Пароль успешен')
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование спец символов
try:
    register_user("JRRRf3343ff")
    print('Пароль успешен')
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование нижнего регистра
try:
    register_user("JRRRF34ED44444")
    print('Пароль успешен')
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование длинны
try:
    register_user("Jа@4")
    print('Пароль успешен')
except ValueError as e:
    print(f"Ошибка: {e}")

"""
Часть 2
Цель задания:
Необходимо создать два декоратора для валидации пользовательских данных перед их сохранением в CSV формате.

Первый декоратор ( password_validator ) проверяет:
    Сложность пароля.
    Включая его длину.
    Количество букв верхнего и нижнего регистра.
    Количество спец-знаков.

Второй декоратор ( username_validator ) проверяет, что в имени пользователя отсутствуют пробелы.
Создайте функцию ( register_user ), которая принимает имя пользователя и пароль, и дозаписывает их в CSV файл, 
обернув ее обоими декораторами.

Требования:
1. Декоратор password_validator:
    Принимает параметры: min_length (минимальная длина пароля, по умолчанию 8),
    min_uppercase (минимальное количество букв верхнего регистра, по умолчанию 1),
    min_lowercase (минимальное количество букв нижнего регистра, по умолчанию 1),
    min_special_chars (минимальное количество спец-знаков, по умолчанию 1).
    Проверяет, соответствует ли пароль заданным критериям.
    Если пароль не соответствует критериям, выбрасывает ValueError с описанием того, что именно не выполнено.
2. Декоратор username_validator:
    Не принимает параметров.
    Проверяет, что в имени пользователя отсутствуют пробелы.
    Если в имени пользователя есть пробелы, выбрасывает ValueError с подробным описанием проблемы.
3. Функция register_user:
    Принимает две строки: username (имя пользователя) и password (пароль).
    Дозаписывает имя пользователя и пароль в CSV файл.
    Оборачиваем функцию обоими декораторами для валидации введенных данных.

Требования к коду:
    Проект должен быть оформлен согласно стандарту PEP-8.
    Все функции и переменные должны быть аннотированы.
    Должны присутствовать док-стринги для всех функций и декораторов.
    Код должен успешно проходить проверку типов с использованием Mypy.
    Все должно работать и все проверки в коде присутствовать.
    Опционально: И да прибудет с вами Замыкание.
"""


def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special: int = 1) -> Callable:
    """
    Функция-декоратор принимает значения и проверяет по ним входящий пароль
    :param length: минимальная длина пароля
    :param uppercase: обязательное количество букв верхнего регистра
    :param lowercase: обязательное количество букв нижнего регистра
    :param special: обязательное количество специальных символов
    """

    def password_checker(func: Callable) -> Callable:
        """
        Функция-декоратор принимает ссылку на ф-ю и возвращает ссылку
        :param func: ccылка на ф-ию
        """
        def wrapper(login: str, password: str) -> Callable:
            """
            Функция принимает 2 аргумента и возвращает ссылку
            :param login: строка Имя пользователя
            :param password: строка Пароль
            """

            count_uppercase: int = sum(1 for letter in str(password) if letter.isupper() == True)
            count_lowercase: int = sum(1 for letter in str(password) if letter.islower() == True)
            count_special: int = sum(1 for letter in str(password) if letter in spec_char)

            if (len(password)) <= length:
                raise ValueError(f'\nПароль {password} слишком короткий. Минимум {length} символов.')
            elif count_uppercase < uppercase:
                raise ValueError(
                    f'\nПароль {password} не содержит минимум {uppercase} символов верхнего регистра.')
            elif count_lowercase < lowercase:
                raise ValueError(
                    f'\nПароль {password} не содержит минимум {lowercase} символов нижнего регистра.')
            elif count_special < special:
                raise ValueError(f'\nПароль {password} не содержит минимум {special} спец знаков.')

            return func(login, password)
        return wrapper
    return password_checker


def user_name_validator(func: Callable) -> Callable:
    """
    Функция принимает ссылку на ф-ию и возвращает ссылку
    :param func: ссылка на функцию
    """
    def wrapper(login: str, password: str) -> Callable:
        """
        Функция принимает 2 аргумента и возвращает функцию
        :param login: строка Имя пользователя
        :param password: строка Пароль
        """
        if login.count(' ') > 0:
            raise ValueError(f'\nЛогин не должен содержать пробелов.')
        return func(login, password)
    return wrapper


@password_validator(8, 1, 1, 1)
@user_name_validator
def register_user(login: str, password: str) -> None:
    """
    Функция принимает 2 аргумента и записывает их в файл login_data.csv
    :param login: строка Имя пользователя
    :param password: строка Пароль
    """

    with open('login_data.csv', 'a', newline='') as file:
        data = csv.writer(file)
        data.writerow([login, password])
    print(f'Логин и пароль записаны в файл {file.name}')


# ПРОВЕРКИ
# Тестирование успешного случая
try:
    register_user("JohnDoe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по паролю
try:
    register_user("JohnDoe", "Pa123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по юзернейму
try:
    register_user("John Doe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")