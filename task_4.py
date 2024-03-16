import csv


def generate_password(name, planet):
    """Generate password

    Keyword arguments:
    name -- ShipName
    planet -- planet from row
    """
    # Извлекаем код корабля
    code = name.split("-")[0]

    # Генерируем пароль в соответствии с условием
    password = (
            planet[-3:] +
            code[len(code) // 2 - 1] + code[len(code) // 2] +
            planet[:3][::-1]
    )
    # Возвращаем в верхнем регистре
    return password.upper()


# Чтение исходного файла
with open("space.txt", "r", encoding="utf-8") as csvfile:
    # Формат переменной data: list[dict[str, str]]
    data = list(csv.DictReader(csvfile, delimiter="*"))

# Обработка строк и запись в конечный файл
with open("space_uniq_password.csv", "w", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, lineterminator="\r")
    writer.writerow(list(data[0].keys()) + ['password'])

    for row in data:
        # Создание пароля
        row['password'] = generate_password(row["ShipName"], row["planet"])
        # Запись в конечный файл
        writer.writerow(row.values())
