"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


user_list = [
        {'name': 'Nastya', 'age': '20', 'job': 'programmist'},
        {'name': 'Ivan', 'age': '36', 'job': 'lawyer'},
        {'name': 'Kate', 'age': '54', 'job': 'seller'},
        {'name': 'Mike', 'age': '67', 'job': 'doctor'},
    ]

import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in user_list:
            writer.writerow(user) 

if __name__ == "__main__":
    main()

        