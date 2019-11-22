from collections import defaultdict
from dataclasses import dataclass, field


@dataclass(frozen=True, eq=True)
class Car:
    registration_number: str
    color: str


@dataclass(frozen=True, eq=True)
class Ticket:
    """
    This class will act as glue (encapsulates relationship) between ParkingLot and a Car
    """
    car: Car
    slot: int


@dataclass
class ParkingLot:
    size: int
    next_available: int = 0
    slots: list = field(init=False)

    def __post_init__(self):
        self.slots = [None] * self.size
        # Using these as an index for fast execution of color
        # and registration lookups
        self.color_index = defaultdict(dict)
        self.car_index = {}

    def is_full(self):
        """
        :return: True if there are no vacant slots, False otherwise.
        """
        return len(self.car_index) == self.size

    def find_next_available_slot(self):
        """
        :return: Slot number of the nearest available slot. `None` if
                 no slot is available.
        """
        if self.is_full(): return None

        for slot_number, slot_content in enumerate(self.slots):
            if slot_content is None: return slot_number

    def park(self, car: Car):
        """
        Parks the car to the next available slot if present. Updates the
        `color_index` and `car_index` accordingly.
        :param car: Instance of `Car`
        :return: Ticket if the car is slot is available, None otherwise.
        """
        next_available_slot = self.find_next_available_slot()
        if next_available_slot is None:
            return None

        # Generate a ticket
        ticket = Ticket(car, next_available_slot + 1)
        # Park the car
        self.slots[next_available_slot] = car

        # Update the indices
        self.car_index[car.registration_number] = ticket
        self.color_index[car.color][ticket] = True
        return ticket

    def evict(self, slot_number: int):
        """
        Creates vacancy for a new car at the given slot number.
        :param slot_number: slot number in the parking lot
        :return: Car object if present at the indicated slot, None otherwise
        """
        if slot_number >= self.size or self.slots[slot_number] is None:
            return None

        car = self.slots[slot_number]

        # Create vacancy
        self.slots[slot_number] = None
        # Update the indices
        ticket = self.car_index[car.registration_number]
        del self.car_index[car.registration_number]
        del self.color_index[car.color][ticket]
        return car

    def get_cars_by_color(self, color: str):
        """
        :param color: Color string
        :return: Returns all the parked cars with given color string.
        """
        tickets = self.color_index.get(color)
        if tickets:
            return [ticket.car for ticket in tickets]
        else: return []

    def get_slots_by_color(self, color: str):
        """
        :param color: Color string
        :return: Returns all the slot numbers with given `color` car parked.
        """
        tickets = self.color_index.get(color)
        if tickets:
            return [ticket.slot for ticket in tickets]
        else: return []

    def get_slot_number_for_car(self, registration_number: str):
        """
        :param registration_number:
        :return: An integer representing the slot number where the car is parked.
        """
        ticket = self.car_index.get(registration_number)
        if ticket: return ticket.slot

    def get_parked_cars_information(self):
        """
        :return: The `car_index` maintained by the object instance.
        """
        return self.car_index
