from abc import ABC, abstractmethod


class Courier:
    """Кур'єр."""

    def __init__(self, name, route):
        """Ініціалізує атрибути кур'єра."""
        self.name = name
        self.route = route


class Shipment(ABC):
    """Абстрактний контракт відправлення."""

    def __init__(self, number, city, courier):
        """Ініціалізує спільні атрибути."""
        self.number = number
        self.city = city
        self.courier = courier

    @abstractmethod
    def tracking_step(self):
        """Кожен нащадок визначає власний крок відстеження."""
        raise NotImplementedError

    def summary(self):
        """Спільний конкретний метод базового класу."""
        return f"№ {self.number}, {self.city}, кур'єр {self.courier.name}"


class ParcelDelivery(Shipment):
    """Доставка посилки."""

    def __init__(self, number, city, courier, weight):
        """Ініціалізує базову частину та вагу."""
        super().__init__(number, city, courier)
        self.weight = weight

    def tracking_step(self):
        """Повертає крок відстеження для посилки."""
        return f"Посилка {self.weight} кг: передати кур'єру на маршрут"


class DocumentDelivery(Shipment):
    """Доставка документів."""

    def __init__(self, number, city, courier, pages):
        """Ініціалізує базову частину та кількість аркушів."""
        super().__init__(number, city, courier)
        self.pages = pages

    def tracking_step(self):
        """Повертає крок відстеження для документів."""
        return f"Документи ({self.pages} арк.): вручити під підпис"


class BrokenDelivery(Shipment):
    """Неповний нащадок: абстрактний метод не реалізовано."""


courier1 = Courier("Іван Петренко", "Львів – Дрогобич")
courier2 = Courier("Олег Коваль", "Київ – Біла Церква")

shipments = [
    ParcelDelivery(1001, "Львів", courier1, 2.5),
    ParcelDelivery(1002, "Київ", courier2, 10.0),
    DocumentDelivery(2001, "Львів", courier1, 12),
]

for item in shipments:
    print(item.summary(), "-", item.tracking_step())

try:
    Shipment(1, "Одеса", courier1)
except TypeError as error:
    print("\nБазовий клас:", error)

try:
    BrokenDelivery(2, "Одеса", courier1)
except TypeError as error:
    print("Неповний нащадок:", error)
