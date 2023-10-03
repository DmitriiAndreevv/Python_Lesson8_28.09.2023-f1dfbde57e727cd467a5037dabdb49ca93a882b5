# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv

def convert_pickle_to_csv(pickle_file_path, csv_file_path):
    try:
        # Читаем данные из pickle файла
        with open(pickle_file_path, 'rb') as pickle_file:
            data = pickle.load(pickle_file)

        if not data or not isinstance(data, list) or not isinstance(data[0], dict):
            print("Некорректный формат данных в pickle файле.")
            return

        # Получаем заголовки столбцов из ключей первого словаря
        fieldnames = data[0].keys()

        # Записываем данные в CSV файл
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Данные из {pickle_file_path} успешно записаны в {csv_file_path}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

# Пример использования функции
pickle_file_path = 'E:\GigBrains\Python 2/output.pickle'
csv_file_path = 'E:\GigBrains\Python 2/output.csv'
convert_pickle_to_csv(pickle_file_path, csv_file_path)