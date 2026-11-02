parcels = [
    {"number": 1001, "weight": 2.5, "city": "Львів"},
    {"number": 1002, "weight": 10.0, "city": "Київ"},
    {"number": 1003, "weight": 0.8, "city": "Львів"},
]


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
show_parcels(find_by_city(parcels, "Одеса"))  

print("\nКур'єри:")
show_couriers(couriers)
