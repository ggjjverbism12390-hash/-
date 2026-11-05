from abc import ABC, abstractmethod


class Courier:
    """Кур'єр."""

    def __init__(self, name, route):
        """Ініціалізує атрибути кур'єра."""
        self.name = name
        self.route = route


class Route:
    """Маршрут доставки: компонент для композиції."""

    def __init__(self, stops):
        """Зберігає список зупинок і поточну позицію."""
        self.stops = list(stops)
        self.position = 0

    def current(self):
        """Повертає поточну зупинку."""
        return self.stops[self.position]

    def advance(self):
        """Переходить до наступної зупинки, якщо вона є."""
        if self.position < len(self.stops) - 1:
            self.position += 1
        return self.current()

    def describe(self):
        """Повертає маршрут одним рядком."""
        return " – ".join(self.stops)


class MovementLogMixin:
    """Mixin: додає журнал переміщень."""

    def __init__(self, *args, **kwargs):
        """Кооперативно викликає наступний клас у MRO та створює журнал."""
        super().__init__(*args, **kwargs)
        self.movement_log = []

    def log_move(self, place):
        """Додає запис про переміщення."""
        self.movement_log.append(place)

    def movement_report(self):
        """Повертає журнал переміщень одним рядком."""
        if not self.movement_log:
            return "Переміщень немає"
        return " -> ".join(self.movement_log)


class Shipment(ABC):
    """Абстрактне відправлення."""

    def __init__(self, number, city, courier):
        """Ініціалізує спільні атрибути."""
        self.number = number
        self.city = city
        self.courier = courier

    @abstractmethod
    def tracking_step(self):
        """Повертає крок відстеження."""
        raise NotImplementedError


class ParcelDelivery(MovementLogMixin, Shipment):
    """Посилка: mixin для журналу та композиція з Route."""

    def __init__(self, number, city, courier, weight, route):
        """Ініціалізує посилку, зберігає маршрут як компонент."""
        super().__init__(number, city, courier)
        self.weight = weight
        self.route = route
        self.log_move(route.current())

    def move_next(self):
        """Делегує перехід маршруту та записує його в журнал."""
        place = self.route.advance()
        self.log_move(place)
        return place

    def tracking_step(self):
        """Повертає поточний крок за маршрутом."""
        return f"Посилка {self.weight} кг, зараз: {self.route.current()}"


class DocumentDelivery(Shipment):
    """Доставка документів без додаткових ролей."""

    def __init__(self, number, city, courier, pages):
        """Ініціалізує базову частину та кількість аркушів."""
        super().__init__(number, city, courier)
        self.pages = pages

    def tracking_step(self):
        """Повертає крок відстеження для документів."""
        return f"Документи ({self.pages} арк.): вручити під підпис"


courier1 = Courier("Іван Петренко", "Львів – Дрогобич")
route = Route(["Львів", "Самбір", "Дрогобич"])
parcel = ParcelDelivery(1001, "Дрогобич", courier1, 2.5, route)
document = DocumentDelivery(2001, "Львів", courier1, 12)

print("MRO:", [cls.__name__ for cls in ParcelDelivery.mro()])
print("Маршрут:", parcel.route.describe())
print(parcel.tracking_step())
parcel.move_next()
parcel.move_next()
print(parcel.tracking_step())
print("Журнал:", parcel.movement_report())
print(document.tracking_step())
print("Документи мають журнал:", hasattr(document, "movement_log"))
