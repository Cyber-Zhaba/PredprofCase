import csv


def sort(lst):
    """List inplace Sort in O(N2) complexity

    Keyword arguments:
    lst -- list of ShipNames
    """
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if int(lst[i].split("-")[1]) > int(lst[j].split("-")[1]):
                lst[i], lst[j] = lst[j], lst[i]


# Чтение исходного файла
with open("space.txt", "r", encoding="utf-8") as csvfile:
    # Формат переменной data: list[dict[str, str]]
    data = list(csv.DictReader(csvfile, delimiter="*"))

    # Получаем именна кораблей
    names = [data[i]["ShipName"] for i in range(len(data))]

    # Сортируем
    # Функция sort() работает inplace
    # То есть все операции изменений проводятся на исходном списке
    sort(names)

    # Выводим первые десять названий
    # Разделитель - новая строка
    print(*names[:10], sep="\n")
