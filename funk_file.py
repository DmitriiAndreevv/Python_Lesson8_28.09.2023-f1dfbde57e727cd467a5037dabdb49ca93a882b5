# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

def convert_text_to_json(input_file, output_file):
    # Открываем текстовый файл для чтения
    with open(input_file, 'r', encoding='utf-8') as text_file:
        lines = text_file.readlines()

    data = []

    # Парсим строки и создаем список словарей
    for line in lines:
        parts = line.strip().split(' - ')
        if len(parts) == 2:
            name, number = parts
            name = name.capitalize()  # Имена с большой буквы
            data.append({"Name": name, "Number": int(number)})

    # Записываем данные в формате JSON в новый файл
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_file = "input.txt"  # Путь к существующему текстовому файлу
    output_file = "output.json"  # Путь к новому файлу в формате JSON
    convert_text_to_json(input_file, output_file)
