"""
Колесников Павел.
HW-5 от 21.12.2023
Секретное послание
"""
# Секретное послание
secret_letter = [
['DFВsjl24sfFFяВАДОd24fssflj234'],
['asdfFп234рFFdо24с$#afdFFтasfо'],
['оafбasdf%^о^FFжа$#af243ю'],
['afпFsfайFтFsfо13н'],
['fн13Fа1234де123юsdсsfь'],
['чFFтF#Fsfsdf$$о'],
['и$##sfF'],
['вSFSDам'],
['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
['FFэasdfтDFsfоasdfFт'],
['FяDSFзFFsыSfкFFf']]

# Список с маленькими русскими буквами
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# Пустой список куда будет сливаться расшифровка
transcript_letter = ''

for secret_list in secret_letter:  # Для каждого отдельного списка в secret_letter
    transcript_letter += ' '  # Для пробелов между отдельными списками = словами в итоговом тексте
    for secret_simbol in ''.join(secret_list):  # И для каждого элемента отдельного списка (преобразуем список в строку)
        for small_rus_simbol in ''.join(small_rus):  # И для каждого элемента списка с русскими буквами (преобразуем список в строку)
            if small_rus_simbol == secret_simbol:  # Если буквы совпадают, то записываем их в пустой список
                transcript_letter += f'{small_rus_simbol}'
                    
print(transcript_letter.lstrip())  #Выводим итог, убирая лишний пробел спереди
exit = input('\n\nДля выхода из програмы нажмите Enter')