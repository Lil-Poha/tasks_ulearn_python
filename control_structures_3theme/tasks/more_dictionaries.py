"""
Увидев какой некрасивый текст находится внутри ячеек, Васе дали задание убрать весь мусор из строк и реализовать хранение данных в более читаемой сущности.

Ему нужно дописать решение прошлой задачи. Необходимо преобразовать каждый вложенный список в словарь, где ключом является название столбца csv, а значением пересечение столбца с текущей строкой.

Дополнительные требования:

    Если значение содержит \n (перенос строки), то его нужно разбить на список
    У всех значений (внутри вложенных списков тоже) должны удаляться пробелы (в начале, в конце строки и лишние по середине). А так же они должны быть очищены от HTML тегов.
    Вывод всех полей в формате key: value
    Если значение поля пустое, то в значении выводить "Нет данных"
    Вложенные списки должны выводиться через точку с запятой
    Между отдельными объектами одна пустая строка (подробнее в Формате вывода)

Прочитав все требования, Вася изрядно понервничал, но решил, что доведёт дело до конца!
Формат ввода

В csv-файле используется следующая структура:

name,key_skills,premium,employer_name,salary_from,salary_to,area_name
Программист,"Информационные технологии
Автоматизированное рабочее место (АРМ)",FALSE,Контур,70000,110000,Москва
Инженер,"Ответственность
Работа в команде
Умение работать руками
пунктуальность
Ответственный подход к работе",FALSE,Сервисный центр ЭКСПЕРТ,30000,60000,Санкт-Петербург

Скачать пример файла
Формат вывода

name: Программист
key_skills: Информационные технологии; Автоматизированное рабочее место (АРМ)
premium: FALSE
employer_name: Контур
salary_from: 70000
salary_to: 110000
area_name: Москва

name: Инженер
key_skills: Ответственность; Работа в команде; Умение работать руками; пунктуальность; Ответственный подход к работе
premium: FALSE
employer_name: Сервисный центр ЭКСПЕРТ
salary_from: 30000
salary_to: 60000
area_name: Санкт-Петербург
"""

import csv
import re
import os



def clean_value(value):
    value = value.strip()
    value = re.sub(r'<[^>]+>', '', value).split()
    sep = " ".join(value)
    return sep


current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_dir, 'control_structures_3theme', 'test', 'more_dictionaries.csv')
with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    header_length = len(headers)
    filter_vacation = [row for row in csv_reader if len([sprint for sprint in row if sprint]) >= header_length / 2]
    for index_row, row in enumerate(filter_vacation):
        dictionary_with_vacancies = {}
        for i_index, i_value in enumerate(row):
            if i_value.find('\n') != -1:
                new_line = i_value.replace('\n', '; ')
            else:
                new_line = i_value
            dictionary_with_vacancies[headers[i_index]] = new_line
        for headers_index,items_vacationary in dictionary_with_vacancies.items():
            print(f'{clean_value(headers_index)}: {clean_value(items_vacationary) if items_vacationary else "Нет данных"}')
        if index_row != len(filter_vacation) - 1:
            print()