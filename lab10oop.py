class AppSettings:
    """Singleton: спільні налаштування служби доставки."""

    _instance = None

    def __new__(cls):
        """Створює єдиний екземпляр і задає значення за замовчуванням."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.base_price = 50.0
            cls._instance.currency = "грн"
        return cls._instance


class ParcelDelivery:
    """Доставка посилки."""

    def __init__(self, number, city, weight):
        """Ініціалізує атрибути посилки."""
        self.number = number
        self.city = city
        self.weight = weight


class DocumentDelivery:
    """Доставка документів."""

    def __init__(self, number, city, pages):
        """Ініціалізує атрибути документів."""
        self.number = number
        self.city = city
        self.pages = pages

    @property
    def weight(self):
        """Повертає орієнтовну вагу документів у кілограмах."""
        return self.pages * 0.005


class ParcelFactory:
    """Фабрика: створює потрібний вид відправлення за ключем."""

    _types = {"parcel": ParcelDelivery, "document": DocumentDelivery}

    @classmethod
    def create(cls, kind, number, city, **details):
        """Повертає екземпляр зареєстрованого класу."""
        try:
            delivery_type = cls._types[kind]
        except KeyError as exc:
            raise ValueError(f"Невідомий тип: {kind}") from exc
        return delivery_type(number, city, **details)


class StandardStrategy:
    """Стратегія стандартної доставки."""

    def estimate(self, shipment):
        """Повертає вартість і термін у днях."""
        settings = AppSettings()
        cost = settings.base_price + 10 * shipment.weight
        return cost, 3


class UrgentStrategy:
    """Стратегія термінової доставки."""

    def estimate(self, shipment):
        """Повертає подвійну вартість і термін у днях."""
        settings = AppSettings()
        cost = (settings.base_price + 10 * shipment.weight) * 2
        return cost, 1


class DeliveryProcessor:
    """Делегує розрахунок переданій стратегії (композиція)."""

    def __init__(self, strategy):
        """Зберігає стратегію як залежність."""
        self.strategy = strategy

    def process(self, shipment):
        """Повертає рядок із розрахунком для відправлення."""
        cost, days = self.strategy.estimate(shipment)
        currency = AppSettings().currency
        return f"№ {shipment.number} ({shipment.city}): {cost:.2f} {currency}, {days} дн."


def report(processor, items):
    """Клієнтський код: однаковий для будь-якої стратегії."""
    for item in items:
        print(processor.process(item))


items = [
    ParcelFactory.create("parcel", 1001, "Львів", weight=2.5),
    ParcelFactory.create("document", 2001, "Київ", pages=200),
]

processor = DeliveryProcessor(StandardStrategy())
print("Стандартна доставка:")
report(processor, items)

processor.strategy = UrgentStrategy()
print("\nТермінова доставка:")
report(processor, items)

try:
    ParcelFactory.create("drone", 3001, "Одеса")
except ValueError as error:
    print("\nПомилка фабрики:", error)

first = AppSettings()
second = AppSettings()
print("Один екземпляр:", first is second)
first.base_price = 60.0
print("Ціна через другий доступ:", second.base_price)