class DeliveryError(Exception):
    """Базовий виняток предметної області служби доставки."""


class ParcelNotFoundError(DeliveryError):
    """Посилку з указаним номером не знайдено."""


class InvalidDeliveryStateError(DeliveryError):
    """Статус невідомий або перехід між статусами заборонений."""


class Parcel:
    """Посилка зі статусом доставки."""

    def __init__(self, number, city, status="нове"):
        """Ініціалізує атрибути посилки."""
        self.number = number
        self.city = city
        self.status = status

    def info(self):
        """Повертає стисле подання посилки."""
        return f"№ {self.number} ({self.city}) [{self.status}]"


class DeliveryService:
    """Надає пошук посилок і зміну їх статусу."""

    valid_statuses = {"нове", "в дорозі", "доставлене"}
    transitions = {
        "нове": {"в дорозі"},
        "в дорозі": {"доставлене"},
        "доставлене": set(),
    }

    def __init__(self, parcels):
        """Зберігає посилки у словнику за номером."""
        self.parcels = {parcel.number: parcel for parcel in parcels}

    def find_parcel(self, number):
        """Повертає посилку або піднімає предметний виняток."""
        try:
            return self.parcels[number]
        except KeyError as exc:
            raise ParcelNotFoundError(f"Посилку № {number} не знайдено") from exc

    def change_status(self, number, status):
        """Змінює статус із перевіркою значення та допустимого переходу."""
        if status not in self.valid_statuses:
            raise InvalidDeliveryStateError(f"Невідомий статус: {status}")
        parcel = self.find_parcel(number)
        if status not in self.transitions[parcel.status]:
            raise InvalidDeliveryStateError(
                f"Перехід «{parcel.status}» -> «{status}» заборонений"
            )
        parcel.status = status
        return parcel


def try_change(service, number, status):
    """Клієнтський сценарій: обробляє очікувані помилки та завжди завершується."""
    try:
        parcel = service.change_status(number, status)
    except ParcelNotFoundError as error:
        print("Пошук:", error, "| причина:", repr(error.__cause__))
    except InvalidDeliveryStateError as error:
        print("Стан:", error)
    else:
        print("Успіх:", parcel.info())
    finally:
        print("Операцію завершено\n")


service = DeliveryService([Parcel(1001, "Львів"), Parcel(1002, "Київ")])

try_change(service, 1001, "в дорозі")
try_change(service, 1001, "нове")
try_change(service, 1002, "загублене")
try_change(service, 999, "в дорозі")
