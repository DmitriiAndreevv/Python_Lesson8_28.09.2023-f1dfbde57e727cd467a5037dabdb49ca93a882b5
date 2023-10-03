# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle

def convert_json_to_pickle(directory):
    # Проверяем, существует ли указанная директория
    if not os.path.exists(directory):
        print(f"Директория '{directory}' не существует.")
        return

    # Получаем список файлов в указанной директории
    file_list = os.listdir(directory)

    # Проходимся по всем файлам в директории
    for filename in file_list:
        # Проверяем, что файл имеет расширение .json
        if filename.endswith('.json'):
            # Формируем полный путь к JSON файлу
            json_file_path = os.path.join(directory, filename)

            # Определяем имя для pickle файла (без расширения)
            pickle_filename = os.path.splitext(filename)[0] + '.pickle'
            pickle_file_path = os.path.join(directory, pickle_filename)

            # Читаем JSON файл
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                json_data = json.load(json_file)

            # Сохраняем содержимое JSON файла в виде pickle
            with open(pickle_file_path, 'wb') as pickle_file:
                pickle.dump(json_data, pickle_file)

            print(f"Сохранено в {pickle_filename}")

# Пример использования функции
directory_path = 'E:\GigBrains\Python 2'
convert_json_to_pickle(directory_path)