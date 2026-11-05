class Courier:
    """Кур'єр (клас із лабораторних № 02-03)."""

    def __init__(self, name, route):
        """Ініціалізує атрибути кур'єра."""
        self.name = name
        self.route = route

    def info(self):
        """Повертає стислий опис кур'єра."""
        return f"Кур'єр {self.name}, маршрут: {self.route}"


class Shipment:
    """Базовий клас відправлення зі спільними атрибутами та контрольованим статусом."""

    valid_statuses = {"нове", "в дорозі", "доставлене"}
    created_count = 0  

    def __init__(self, number, city, courier, status="нове"):
        """Ініціалізує спільну для всіх відправлень частину."""
        self.number = number
        self.city = city
        self.courier = courier
        self._status = "нове"
        self.status = status 
        Shipment.created_count += 1

    @property
    def status(self):
        """Повертає поточний статус відправлення."""
        return self._status

    @status.setter
    def status(self, value):
        """Дозволяє встановити лише статус зі списку valid_statuses."""
        if value not in self.valid_statuses:
            raise ValueError(f"Невідомий статус: {value}")
        self._status = value

    def summary(self):
        """Повертає спільну для всіх відправлень інформацію."""
        return (
            f"Відправлення № {self.number} до міста {self.city} "
            f"[{self.status}], {self.courier.name}"
        )


class ParcelDelivery(Shipment):
    """Доставка посилки: додає вагу, перевіряє її допустиме значення."""

    MAX_WEIGHT = 30.0 

    def __init__(self, number, city, courier, weight, status="нове"):
        """Ініціалізує базову частину через super(), потім власну вагу."""
        super().__init__(number, city, courier, status)
        self._weight = None
        self.weight = weight  

    @property
    def weight(self):
        """Повертає вагу посилки в кілограмах."""
        return self._weight

    @weight.setter
    def weight(self, value):
        """Встановлює вагу, якщо 0 < value <= MAX_WEIGHT."""
        if not isinstance(value, (int, float)) or not 0 < value <= self.MAX_WEIGHT:
            raise ValueError(f"Недопустима вага: {value}")
        self._weight = value

    def weight_info(self):
        """Повертає інформацію про вагу посилки."""
        return f"Вага посилки: {self.weight} кг"


class DocumentDelivery(Shipment):
    """Доставка документів: додає кількість аркушів і ознаку конфіденційності."""

    def __init__(self, number, city, courier, pages, confidential=False, status="нове"):
        """Ініціалізує базову частину через super(), потім власні атрибути."""
        super().__init__(number, city, courier, status)
        self.pages = pages
        self.confidential = confidential

    def document_info(self):
        """Повертає інформацію про документи."""
        mark = "конфіденційні" if self.confidential else "звичайні"
        return f"Документи: {self.pages} арк., {mark}"

courier1 = Courier("Іван Петренко", "Львів – Дрогобич")
courier2 = Courier("Олег Коваль", "Київ – Біла Церква")

parcel_a = ParcelDelivery(1001, "Львів", courier1, 2.5)
parcel_b = ParcelDelivery(1002, "Київ", courier2, 10.0, "в дорозі")
doc_a = DocumentDelivery(2001, "Львів", courier1, 12, True)
doc_b = DocumentDelivery(2002, "Київ", courier2, 3)

print("Посилки:")
for item in (parcel_a, parcel_b):
    print(item.summary()) 
    print("  ", item.weight_info())  

print("\nДокументи:")
for item in (doc_a, doc_b):
    print(item.summary())
    print("  ", item.document_info())

doc_a.status = "доставлене"
print("\nПісля зміни статусу:", doc_a.summary())

try:
    parcel_a.status = "загублене"
except ValueError as error:
    print("Помилка статусу:", error)

try:
    parcel_a.weight = 100
except ValueError as error:
    print("Помилка ваги:", error)

print("\nParcelDelivery є Shipment:", isinstance(parcel_a, Shipment))
print("DocumentDelivery є Shipment:", isinstance(doc_a, Shipment))
print("DocumentDelivery є ParcelDelivery:", isinstance(doc_a, ParcelDelivery))
print("Створено відправлень:", Shipment.created_count)
