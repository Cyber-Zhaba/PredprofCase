import csv

# Чтение исходного файла
with open("space.txt", "r", encoding="utf-8") as csvfile:
    # Формат переменной data: list[dict[str, str]]
    data = list(csv.DictReader(csvfile, delimiter="*"))
    data_by_name = {
        data[i]['ShipName']: (data[i]['planet'], data[i]['direction'])
        for i in range(len(data))
    }


while True:
    # Чтение ввода
    name = input()

    # Обработка остановки
    if name.lower() == "stop":
        break

    # Получение данных из словаря
    row = data_by_name.get(name, None)

    # Обработка ошибки
    if row is None:
        print("error.. er.. ror..")
        break

    # Вывод
    print(f"Корабль {name} был отправлен с планеты: {row[0]} и его направление движения было: {row[1]}")
