"""
Вася несколько дней без еды и отдыха составлял базу данных о вакансиях в csv-файл и, когда уже составил,
узнал об изменении стандартов записи. Пока Вася лежит в обмороке, поменяйте все записи в файле на необходимый формат.

На сайте стандарта по оформлению базы данных в csv формате вышла инструкция, в каком порядке нужно применять изменения:

    Необходимо поменять всё время, записанное в формате HH.ii (14.00) на HH:ii (14:00)

    Убрать из текста все HTML-теги (например, <p>)

    Поменять все конструкции дата-время следующего вида YYYY-mm-ddTHH:ii:ss+ZZZZ (2017-06-26T15:00:03+0300) на формат
    HH:ii:ss dd/mm/YYYY (15:00:03 26/06/2017)

Перед падением в обморок Вася решил выделить ключевые слова вакансий: все слова, идентичные или частично содержащие
ключевое слово (независимо от регистра) должны быть выделены заглавными буквами.

Например:

# ключевое слово "exam"
here some example for your Exam -> here some EXAMPLE for your EXAM

# ключевое слово "раб"
Вася решил устроиться на работу Python-Разработчиком ->
Вася решил устроиться на РАБОТУ Python-РАЗРАБОТЧИКОМ

# ключевое слово "сок"
Вася съел кусок торта, запил его апельсиновым соком, сидя на высокой табуретке ->
Вася съел КУСОК торта, запил его апельсиновым СОКОМ, сидя на ВЫСОКОЙ табуретке

Формат ввода

Первой строкой на вход подаётся название искомого csv-файла.

Второй строкой подаётся название, под которым необходимо сохранить требуемый csv-файл, учитывающий все требования.

Третьей строкой подаются ключевые слова, которые необходимо выделить в файле. Если слово в тексте содержит
ключевое слово (ключевое слово является подстрокой слова из текста), его также необходимо выделить.
Ключевые слова разделены запятой.

example.csv
my_answer.csv
exam,answer,vasya

Пример формата текста искомого csv-файла

Преподаватель программирования,"<p>Увлечён программированием, компьютерными играми? Предлагаем познакомить детей с миром
программирования и проводить занятия так, чтобы ребенку хотелось погружаться ещё и ещё!</p>","Преподаватель
Организация учебного процесса
Обучение
HTML
CSS",noExperience,False,СФЕРА,20000.0,50000.0,False,RUR,Тюмень,2021-10-18T19:22:07+0300

Пример формата текста результирующего файла

Преподаватель ПРОГРАММИРОВАНИЯ,"Увлечён ПРОГРАММИРОВАНИЕМ, компьютерными играми? Предлагаем познакомить детей с миром
ПРОГРАММИРОВАНИЯ и проводить занятия так, чтобы ребенку хотелось погружаться ещё и ещё!","Преподаватель
Организация учебного процесса
Обучение
HTML
CSS",noExperience,False,СФЕРА,20000.0,50000.0,False,RUR,Тюмень,19:22:07 18/10/2021
"""


import csv
import re
import os

def replace_time_format(text):
    return re.sub(r'([0-9]).([0-6][0-9])' or '[0-2][0-9].[0-6][0-9]', lambda m: m.group().replace(".", ":"), text)

def remove_html_tags(text):
    return re.sub(r'<[^>]+>', '', text)

def replace_datetime_format(text):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}:\d{2}:\d{2})\+\d{4}', r'\4 \3/\2/\1', text)

def highlight_keywords(text, keywords):
    for keyword in keywords:
        pattern = re.compile(r'\b\w*' + re.escape(keyword) + r'\w*\b', re.IGNORECASE)
        text = pattern.sub(lambda x: x.group(0).upper(), text)
    return text


current_dir1 = os.path.dirname(os.path.abspath(__file__))
project_dir1 = os.path.dirname(os.path.dirname(current_dir1))
file = os.path.join(project_dir1, 'strings_and_regular_expressions_4theme', 'test', 'change_csv.csv')
current_dir2 = os.path.dirname(os.path.abspath(__file__))
project_dir2 = os.path.dirname(os.path.dirname(current_dir2))
new_file = os.path.join(project_dir2, 'strings_and_regular_expressions_4theme', 'result', 'change_csv_result.csv')
highlight = input().strip().split(',')

with open(file, mode='r', encoding='utf-8') as infile, open(new_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        writer.writerow(list(map(lambda x: replace_time_format(remove_html_tags(replace_datetime_format(highlight_keywords(x, highlight)))),row)))