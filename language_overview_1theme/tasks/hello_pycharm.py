"""
Вася решил взяться за Python серьёзно! Он установил IDE PyCharm,
создал там новый проект, и вот его встречает приветственный скрипт от PyCharm.
Вася узнал, что конструкция if __name__ == '__main__' - это точка входа программу,
которая запускается только если запускается именно текущий Python-файл.

Изучите подробнее про эту конструкцию и сделайте следующее:
Добавьте в функцию print_hi вывод в консоль глобальной переменной __name__ сразу после строки print(f'Hi, {name}')
Между функцией print_hi и конструкцией if __name__ == '__main__' вставьте вызов функции print_hi с аргументом "Python"

Можете поэкспериментировать с данной конструкцией: создайте у себя два Python скрипта,
в один из них поместите решение к этой задаче, а в другом подключите первый с помощью ключевого слова import.

У вас должно получиться следующее: если вы запустите первый скрипт, то функция print_hi вызовется дважды,
а в результате будут виднеться две строки: "Hi, Python" и "Hi, PyCharm". Если же вы запустите второй скрипт,
то на экран "Hi, PyCharm" не выведется.
"""

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'{__name__}')

print_hi('Python')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/