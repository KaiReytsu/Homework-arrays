# Дана строка, она состоит только из букв английского алфавита.
# 1. сбор статистики: 
#     какие буквы сколько раз встречаются. (Выполнила Крикунова Ю.В.)
# 2. вывод на экран самой часто встречающейся буквы
#     без использования функций max, sorted и т.д.

#Функция анализа строки: сколько раз встречается каждая буква в строке
def letter_cout(string):
    parsed_string = string.lower().split()
    parsed_string = ''.join(parsed_string)
    analysis = {}
    for letter in parsed_string:
        if letter in analysis:
            analysis[letter] += 1
        else:
            analysis[letter] = 1
    return analysis

#В переменной en_string пример строки
en_string = 'There is the house where my family lives'

#Вызова функции
letter_cout(en_string)