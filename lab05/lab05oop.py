class Courier:
    """Кур'єр (клас із попередніх лабораторних)."""

    def __init__(self, name, route):
        """Ініціалізує атрибути кур'єра."""
        self.name = name
        self.route = route


class Shipment:
    """Базовий клас відправлення зі спільним інтерфейсом tracking_step()."""

    valid_statuses = {"нове", "в дорозі", "доставлене"}

    def __init__(self, number, city, courier, status="нове"):
        """Ініціалізує спільну для всіх відправлень частину."""
        self.number = number
        self.city = city
        self.courier = courier
        self._status = "нове"
        self.status = status

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

    def tracking_step(self):
        """Повертає загальний наступний крок залежно від статусу."""
        steps = {
            "нове": "Зареєструвати відправлення",
            "в дорозі": "Передати кур'єру та відстежувати маршрут",
            "доставлене": "Закрити відправлення",
        }
        return steps[self.status]


class ParcelDelivery(Shipment):
    """Доставка посилки."""

    def __init__(self, number, city, courier, weight, status="нове"):
        """Ініціалізує базову частину через super(), потім вагу."""
        super().__init__(number, city, courier, status)
        self.weight = weight

    def tracking_step(self):
        """Перевизначає метод: додає вагу до загального кроку через super()."""
        return f"Посилка {self.weight} кг: " + super().tracking_step().lower()


class DocumentDelivery(Shipment):
    """Доставка документів."""

    def __init__(self, number, city, courier, pages, confidential=False, status="нове"):
        """Ініціалізує базову частину через super(), потім власні атрибути."""
        super().__init__(number, city, courier, status)
        self.pages = pages
        self.confidential = confidential

    def tracking_step(self):
        """Повністю перевизначає метод: свій алгоритм для документів."""
        if self.status == "нове":
            return f"Перерахувати аркуші ({self.pages}) і запечатати конверт"
        if self.status == "в дорозі":
            if self.confidential:
                return "Вручити особисто одержувачу під підпис"
            return "Залишити в канцелярії одержувача"
        return "Отримати підпис про вручення"



courier1 = Courier("Іван Петренко", "Львів – Дрогобич")
courier2 = Courier("Олег Коваль", "Київ – Біла Церква")

shipments = [
    ParcelDelivery(1001, "Львів", courier1, 2.5),
    ParcelDelivery(1002, "Київ", courier2, 10.0, "в дорозі"),
    DocumentDelivery(2001, "Львів", courier1, 12, True, "в дорозі"),
    DocumentDelivery(2002, "Київ", courier2, 3),
    DocumentDelivery(2003, "Львів", courier1, 5, False, "доставлене"),
]


for item in shipments:
    print(f"№ {item.number} [{item.status}]: {item.tracking_step()}")


print("\nПісля зміни статусу першого відправлення:")
shipments[0].status = "в дорозі"
print(f"№ {shipments[0].number} [{shipments[0].status}]: {shipments[0].tracking_step()}")


try:
    shipments[1].status = "загублене"
except ValueError as error:
    print("\nПомилка статусу:", error)
