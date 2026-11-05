
class Parcel:
    """Посилка з контрольованою вагою."""

    MAX_WEIGHT = 30.0 

    def __init__(self, number, weight, city):
        """Створює посилку; вага проходить перевірку через setter."""
        self.number = number
        self.city = city
        self._weight = None 
        self.weight = weight 

    @property
    def weight(self):
        """Повертає вагу посилки в кілограмах."""
        return self._weight

    @weight.setter
    def weight(self, value):
        """Встановлює вагу, якщо 0 < value <= MAX_WEIGHT."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Вага має бути числом")
        if not 0 < value <= self.MAX_WEIGHT:
            raise ValueError(
                f"Вага має бути в межах (0; {self.MAX_WEIGHT}] кг, отримано: {value}"
            )
        self._weight = value

    def info(self):
        """Повертає стислий опис посилки."""
        return f"Посилка {self.number}: {self.weight} кг, місто: {self.city}"


class Courier:
    """Кур'єр."""

    def __init__(self, name, route):
        """Ініціалізує атрибути кур'єра."""
        self.name = name
        self.route = route

    def info(self):
        """Повертає стислий опис кур'єра."""
        return f"Кур'єр {self.name}, маршрут: {self.route}"


class DeliveryRequest:
    """Заявка на доставку з контрольованим статусом."""

    valid_statuses = {"нова", "в дорозі", "доставлена"}
    created_count = 0  
    def __init__(self, number, parcel, courier, status="нова"):
        """Створює заявку та задає початковий статус через setter."""
        self.number = number
        self.parcel = parcel
        self.courier = courier
        self._status = "нова"
        self.status = status
        DeliveryRequest.created_count += 1

    @property
    def status(self):
        """Повертає поточний статус заявки."""
        return self._status

    @status.setter
    def status(self, value):
        """Дозволяє встановити лише статус зі списку valid_statuses."""
        if value not in self.valid_statuses:
            raise ValueError(f"Невідомий статус: {value}")
        self._status = value

    def summary(self):
        """Формує короткий опис заявки."""
        return (
            f"Заявка {self.number}: {self.parcel.info()} | "
            f"{self.courier.name} [{self.status}]"
        )



parcel1 = Parcel(1001, 2.5, "Львів")
parcel2 = Parcel(1002, 10.0, "Київ")
parcel3 = Parcel(1003, 0.8, "Львів")

courier1 = Courier("Іван Петренко", "Львів – Дрогобич")
courier2 = Courier("Олег Коваль", "Київ – Біла Церква")

request1 = DeliveryRequest(1, parcel1, courier1)
request2 = DeliveryRequest(2, parcel2, courier2, "в дорозі")
request3 = DeliveryRequest(3, parcel3, courier1)


print("Початковий стан:")
for r in (request1, request2, request3):
    print(r.summary())

request1.status = "в дорозі"
parcel3.weight = 1.2

print("\nПісля коректних змін:")
for r in (request1, request2, request3):
    print(r.summary())

print("Створено заявок:", DeliveryRequest.created_count)


print("\nПеревірка помилок:")

try:
    parcel1.weight = -5
except ValueError as error:
    print("Помилка ваги:", error)

try:
    parcel1.weight = 100
except ValueError as error:
    print("Помилка ваги:", error)

try:
    parcel1.weight = "важка"
except TypeError as error:
    print("Помилка типу:", error)

try:
    request2.status = "загублена"
except ValueError as error:
    print("Помилка статусу:", error)

try:
    Parcel(1004, 0, "Одеса") 
except ValueError as error:
    print("Помилка при створенні:", error)


print("\nВага parcel1:", parcel1.weight, "| статус request2:", request2.status)