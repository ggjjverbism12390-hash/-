class Parcel:
    """Посилка з текстовим поданням і рівністю за номером."""

    def __init__(self, number, weight, city):
        """Ініціалізує атрибути посилки."""
        self.number = number
        self.weight = weight
        self.city = city

    def __str__(self):
        """Повертає коротке подання для користувача."""
        return f"Посилка № {self.number}: {self.weight} кг, {self.city}"

    def __repr__(self):
        """Повертає технічне подання для налагодження."""
        return (
            f"{type(self).__name__}(number={self.number!r}, "
            f"weight={self.weight!r}, city={self.city!r})"
        )

    def __eq__(self, other):
        """Вважає посилки рівними, якщо збігаються їхні номери."""
        if not isinstance(other, Parcel):
            return NotImplemented
        return self.number == other.number

    def __hash__(self):
        """Узгоджує хеш із рівністю за номером."""
        return hash(self.number)


class ExpressParcel(Parcel):
    """Термінова посилка з терміном доставки."""

    def __init__(self, number, weight, city, days):
        """Ініціалізує базову частину та термін у днях."""
        super().__init__(number, weight, city)
        self.days = days

    def __str__(self):
        """Додає термін до короткого подання."""
        return super().__str__() + f", експрес {self.days} дн."

    def __repr__(self):
        """Додає термін до технічного подання."""
        return (
            f"{type(self).__name__}(number={self.number!r}, "
            f"weight={self.weight!r}, city={self.city!r}, days={self.days!r})"
        )


first = Parcel(1001, 2.5, "Львів")
same_number = Parcel(1001, 7.0, "Київ")
second = Parcel(1002, 10.0, "Київ")
express = ExpressParcel(1003, 0.8, "Одеса", 1)

print(first)
print(repr(first))
print(express)
print(repr(express))

print("\nОдин номер:", first == same_number)
print("Різні номери:", first == second)
print("Порівняння з рядком:", first == "1001")
print("Порівняння з числом:", first == 1001)

parcels = [first, second, express]
print("\nСписок:", parcels)
print("Є в списку (той самий номер):", same_number in parcels)
print("Індекс express:", parcels.index(ExpressParcel(1003, 5, "Тест", 3)))