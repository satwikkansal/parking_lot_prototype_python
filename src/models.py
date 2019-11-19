from dataclasses import dataclass, field


@dataclass
class Car:
    registration_number: str
    color: str


@dataclass
class ParkingLot:
    size: int
    next_available: int = 0
    available_slots: list = field(init=False)

    def __post_init__(self):
        self.available_slots = [True] * self.size


@dataclass
class Ticket:
    car: Car
    slot: int
