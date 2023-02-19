from dataclasses import dataclass


# Задание 1
@dataclass(frozen=True)
class Technic:
    name: str
    price: int
    existence: bool

    def category(self):
        return 'Дорогой' if self.price >= 50000 else 'Дешевый'

    def __len__(self):
        return len(self.name)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)
