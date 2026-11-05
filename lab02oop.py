class Parcel:
    """Модель однієї посилки."""

    def __init__(self, number, weight, city):
        """Ініціалізує атрибути екземпляра посилки."""
        # Кожен об'єкт зберігає власний стан в атрибутах self.
        self.number = number
        self.weight = weight
        self.city = city

    def info(self):
        """Повертає стислий опис посилки."""
        return f"Посилка {self.number}: {self.weight} кг, місто: {self.city}"

    def change_city(self, city):
        """Змінює місто призначення."""
        self.city = city

class Courier:
    """Модель кур'єра."""

    def __init__(self, name, route):
        """Ініціалізує атрибути екземпляра кур'єра."""
        self.name = name
        self.route = route

    def info(self):
        """Повертає стислий опис кур'єра."""
        return f"Кур'єр {self.name}, маршрут: {self.route}"

    def change_route(self, route):
        """Змінює маршрут кур'єра."""
        self.route = route

parcel1 = Parcel(1001, 2.5, "Львів")
parcel2 = Parcel(1002, 10.0, "Київ")
parcel3 = Parcel(1003, 0.8, "Львів")

courier1 = Courier("Іван Петренко", "Львів – Дрогобич")
courier2 = Courier("Олег Коваль", "Київ – Біла Церква")

print("Початковий стан:")
for parcel in (parcel1, parcel2, parcel3):
    print(parcel.info())
for courier in (courier1, courier2):
    print(courier.info())

parcel1.change_city("Одеса")

print("\nПісля зміни міста першої посилки:")
for parcel in (parcel1, parcel2, parcel3):
    print(parcel.info())

courier1.change_route("Львів – Стрий")

print("\nПісля зміни маршруту першого кур'єра:")
for courier in (courier1, courier2):
    print(courier.info())