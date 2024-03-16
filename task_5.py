import csv

table = {}


def build_table():
    """Build hash table"""
    global table
    # Чтение исходного файла
    with open("space.txt", "r", encoding="utf-8") as csvfile:
        # Формат переменной data: list[dict[str, str]]
        for row in csv.DictReader(csvfile, delimiter="*"):
            table.setdefault(row["planet"], [])
            # Добавление нового коробля
            table[row["planet"]].append(row["ShipName"])


def get_ships(planet):
    """Get ships using planet

    Keyword arguments:
    planet -- planet name from row
    """
    global table
    # Получение кораблей
    ships = table[planet]
    # Вывод
    print(f"{planet}: {' '.join(ships)}")


# Использование

# 1. Строим хеш-таблицу
build_table()

# 2. В цикле вызываем функцию get_ships
names = [
    "Голевард",
    "Угариния",
    "Жезл Саурона",
    "Шамлария",
    "Золотая Даль",
    "Нейландия",
    "Наразиния",
    "Тальсария",
    "Мирондия",
    "Беренс",
]

for name in names:
    get_ships(name)
