"""
Колесников Павел.
HW-3 от 15.12.2023
Палиндромы
"""
word_user = input('Введите слово: ')
if word_user.lower() == word_user[::-1].lower():
    print(f'Слово "{word_user}" является палиндромом')
else:
    print(f'Слово "{word_user}" не является палиндромом')
