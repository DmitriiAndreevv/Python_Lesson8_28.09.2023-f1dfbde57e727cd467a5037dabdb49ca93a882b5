# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def get_directory_info(directory):
    # Инициализируем переменные для хранения информации о директории
    dir_info = {
        'name': os.path.basename(directory),
        'type': 'directory',
        'size': 0  # Начальный размер равен нулю
    }

    # Перебираем содержимое директории
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Если это директория, рекурсивно вызываем функцию для неё
        if os.path.isdir(item_path):
            sub_dir_info = get_directory_info(item_path)
            dir_info['size'] += sub_dir_info['size']  # Увеличиваем размер

        # Если это файл, получаем его размер
        elif os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            dir_info['size'] += file_size  # Увеличиваем размер
            # Создаем информацию о файле
            file_info = {
                'name': item,
                'type': 'file',
                'size': file_size
            }
            # Сохраняем информацию о файле в файлы разных форматов
            save_as_json(file_info, 'file_info.json')
            save_as_csv(file_info, 'file_info.csv')
            save_as_pickle(file_info, 'file_info.pickle')

    # Сохраняем информацию о директории в файлы разных форматов
    save_as_json(dir_info, 'dir_info.json')
    save_as_csv(dir_info, 'dir_info.csv')
    save_as_pickle(dir_info, 'dir_info.pickle')

    return dir_info

def save_as_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_as_csv(data, filename):
    with open(filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if os.path.getsize(filename) == 0:
            writer.writerow(data.keys())  # Записываем заголовок, если файл пустой
        writer.writerow(data.values())

def save_as_pickle(data, filename):
    with open(filename, 'ab') as pickle_file:
        pickle.dump(data, pickle_file)

# Пример использования функции
get_directory_info('D:/GigBrains/Python 2/8')
