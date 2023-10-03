# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json

def process_csv_to_json(input_csv_file, output_json_file):
    # Создаем список для хранения записей в формате JSON
    json_data = []

    # Читаем CSV файл
    with open(input_csv_file, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Пропускаем заголовок

        for row in csv_reader:
            # Получаем данные из CSV строки
            name, user_id, access_level = row

            # Дополняем ID до 10 цифр нулями
            user_id = user_id.zfill(10)

            # Преобразуем первую букву имени в верхний регистр
            name = name.capitalize()

            # Создаем хеш на основе имени и идентификатора
            user_hash = hash(name + user_id)

            # Создаем JSON запись
            user_data = {
                'name': name,
                'user_id': user_id,
                'access_level': access_level,
                'user_hash': user_hash
            }

            # Добавляем запись в список
            json_data.append(user_data)

    # Сохраняем данные в JSON файл
    with open(output_json_file, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

# Пример использования функции
process_csv_to_json('input.csv', 'output.json')
