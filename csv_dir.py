# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle

def read_csv_to_pickle_string(csv_file_path):
    try:
        # Читаем данные из CSV файла
        with open(csv_file_path, mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)

        # Преобразуем данные в строку в формате pickle
        pickle_data = pickle.dumps(data)

        return pickle_data
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return None

# Пример использования функции
csv_file_path = 'E:\GigBrains\Python 2/output.csv'
pickle_data = read_csv_to_pickle_string(csv_file_path)

if pickle_data:
    print(pickle_data)




# десериализовать её обратно в Python-объекты с помощью функции pickle.loads()
# import pickle

# pickle_data = b'\x80\x04\x95...\x94ee.'  # Ваша строка данных pickle

# # Десериализуем данные
# data = pickle.loads(pickle_data)

# # Теперь data содержит исходные данные из CSV файла
# print(data)
