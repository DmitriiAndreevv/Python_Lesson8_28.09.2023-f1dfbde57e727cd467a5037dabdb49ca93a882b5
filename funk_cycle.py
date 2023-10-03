# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


import json

def get_user_info():
    name = input("Введите имя пользователя: ")
    user_id = input("Введите личный идентификатор пользователя: ")
    access_level = int(input("Введите уровень доступа (от 1 до 7): "))
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
            json.dump(user_data, file, indent=4)

if __name__ == "__main__":
    main()
