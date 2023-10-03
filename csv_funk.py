# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json

def save_to_csv(user_data):
    with open("users.csv", "w", newline="") as csvfile:
        fieldnames = ["Name", "User ID", "Access Level"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for access_level, users in user_data.items():
            for user_id, user_info in users.items():
                writer.writerow({
                    "Name": user_info["name"],
                    "User ID": user_id,
                    "Access Level": access_level
                })
def get_user_info():
    name = input("Введите имя пользователя: ")
    user_id = input("Введите личный идентификатор пользователя: ")
    access_level = input("Введите уровень доступа пользователя (от 1 до 7): ")
    return name, user_id, access_level

def main():
    user_data = {}
    try:
        with open("users.json", "r") as file:
            user_data = json.load(file)
    except FileNotFoundError:
        pass

    while True:
        name, user_id, access_level = get_user_info()

        if access_level not in user_data:
            user_data[access_level] = {}

        if user_id in user_data[access_level]:
            print("Пользователь с таким идентификатором уже существует.")
        else:
            user_data[access_level][user_id] = {"name": name}

        with open("users.json", "w") as file:
            json.dump(user_data, file)  # Сохраняем данные в JSON-файл

        save_to_csv(user_data)

if __name__ == "__main__":
    main()