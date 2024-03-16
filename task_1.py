import csv


def two_digits(string):
    """Find first two digits in ShipName

    Keyword arguments:
    string -- ShipName
    """
    first, second = None, None
    for char in string:
        if char.isdigit() and first is None:
            first = int(char)
        elif char.isdigit():
            second = int(char)
            return first, second
    return 0, 0


# Чтение исходного файла
with open("space.txt", "r", encoding="utf-8") as csvfile:
    # Формат переменной data: list[dict[str, str]]
    data = list(csv.DictReader(csvfile, delimiter="*"))

# Обработка строк и запись в конечный файл
with open("space_new.txt", "w", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter="*", lineterminator="\r")
    writer.writerow(data[0].keys())

    for row in data:
        if row["coord_place"] == "0 0":
            # Формируем необхдимые переменные
            n, m = two_digits(row["ShipName"])
            t = len(row["planet"].strip().rstrip())
            dir_x, dir_y = map(int, row["direction"].split())

            # Обработка условия
            if n > 5:
                x = n + dir_x
            else:
                x = - (n + dir_x) * 4 + t
            if m > 3:
                y = m + t + dir_y
            else:
                y = - (n + dir_y) * m

            row["coord_place"] = f"{x} {y}"

        # Вывод на экран информации о короблях, у которых последний элемент кода равен “V”.
        letters = row["ShipName"].split('-')[0]
        if letters[-1] == 'V':
            x, y = row["coord_place"].split()
            print(f" {row["ShipName"]} - ({x}, {y})")

        writer.writerow(row.values())
