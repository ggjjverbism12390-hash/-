DELIVERY_TYPES = {}


def register_delivery(cls):
    """Реєструє клас у реєстрі за атрибутом kind."""
    DELIVERY_TYPES[cls.kind] = cls
    return cls


@register_delivery
class Parcel:
    """Звичайна посилка."""

    kind = "parcel"
    MAX_WEIGHT = 30.0

    def __init__(self, number, weight, city):
        """Створює посилку після перевірки маси."""
        if not Parcel.is_valid_weight(weight):
            raise ValueError(f"Недопустима маса: {weight}")
        self.number = number
        self.weight = weight
        self.city = city

    @staticmethod
    def is_valid_weight(weight):
        """Перевіряє масу без доступу до стану об'єкта."""
        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            return False
        return 0 < weight <= Parcel.MAX_WEIGHT

    @classmethod
    def from_label(cls, label):
        """Створює об'єкт із рядка формату «номер;маса;місто»."""
        number, weight, city = label.split(";")
        return cls(int(number), float(weight), city.strip())

    def __str__(self):
        """Повертає стисле подання посилки."""
        return f"[{self.kind}] № {self.number}: {self.weight} кг, {self.city}"


@register_delivery
class ExpressParcel(Parcel):
    """Термінова посилка."""

    kind = "express"


@register_delivery
class DocumentDelivery:
    """Доставка документів."""

    kind = "document"

    def __init__(self, number, pages, city):
        """Ініціалізує атрибути документів."""
        self.number = number
        self.pages = pages
        self.city = city

    def __str__(self):
        """Повертає стисле подання доставки документів."""
        return f"[{self.kind}] № {self.number}: {self.pages} арк., {self.city}"


print("Маса 2.5 допустима:", Parcel.is_valid_weight(2.5))
print("Маса -1 допустима:", Parcel.is_valid_weight(-1))

parcel = Parcel.from_label("1001; 2.5; Львів")
express = ExpressParcel.from_label("1002;10;Київ")
document = DocumentDelivery(2001, 12, "Львів")

print(parcel)
print(express)
print(document)
print("Тип express:", type(express).__name__)

try:
    Parcel.from_label("1003;100;Одеса")
except ValueError as error:
    print("Помилка:", error)

print("Зареєстровані види доставки:", sorted(DELIVERY_TYPES))
