# Лабораторна робота № 01. Варіант 7. Служба доставки.
# Всі дані вигадані.

# --- Сутність 1: Посилка ---
# Дані (майбутні атрибути класу Parcel): number, weight, city
# Дії (майбутні методи): show(), is_heavy(), change_city()
parcels = [
    {"number": 1001, "weight": 2.5, "city": "Львів"},
    {"number": 1002, "weight": 10.0, "city": "Київ"},
    {"number": 1003, "weight": 0.8, "city": "Львів"},
]

# --- Сутність 2: Кур'єр ---
# Дані (майбутні атрибути класу Courier): name, route
# Дії (майбутні методи): show(), assign_parcel(), change_route()
couriers = [
    {"name": "Іван Петренко", "route": "Львів – Дрогобич"},
    {"name": "Олег Коваль", "route": "Київ – Біла Церква"},
    {"name": "Марія Шевчук", "route": "Львів – Стрий"},
]


def show_parcels(items):
    """Виводить номер, вагу та місто призначення кожної посилки."""
    for item in items:
        print(item["number"], item["weight"], "кг", item["city"])


def find_by_city(items, city):
    """Повертає список посилок із заданим містом призначення."""
    return [item for item in items if item["city"] == city]


def show_couriers(items):
    """Виводить ім'я та маршрут кожного кур'єра."""
    for item in items:
        print(item["name"], "-", item["route"])


# Демонстрація
print("Усі посилки:")
show_parcels(parcels)

print("\nПосилки до міста Львів:")
show_parcels(find_by_city(parcels, "Львів"))

print("\nПосилки до міста Одеса:")
show_parcels(find_by_city(parcels, "Одеса"))  # порожній результат

print("\nКур'єри:")
show_couriers(couriers)

# Класи для лабораторної № 02: Parcel (number, weight, city) і Courier (name, route).
# Функції show_* і find_by_city стануть методами або операціями над колекцією об'єктів.