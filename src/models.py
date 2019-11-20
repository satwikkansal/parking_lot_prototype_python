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
        # Using these as an index for fast execution of color
        # and registration lookups
        self.color_index = {}
        self.car_index = {}

    def park(self, car: Car):
        """
        Parks the car to the next available slot if present. Updates the
        `color_index` and `car_index` accordingly.
        :param car: Instance of `Car`
        :return: Ticket is the car is slot is available, None otherwise.
        """
        pass

    def get_cars_by_color(self, color: str):
        """
        :param color: Color string
        :return: Returns all the parked cars with given color string.
        """
        tickets = self.color_index.get(color)
        if tickets:
            return [ticket.car for ticket in tickets]

    def get_slots_by_color(self, color: str):
        """
        :param color: Color string
        :return: Returns all the slot numbers with given `color` car parked.
        """
        tickets = self.color_index.get(color)
        if tickets:
            return [ticket.car.color for ticket in tickets]

    def get_slot_number_for_car(self, registration_number:str):
        """
        :param registration_number:
        :return: An integer representing the slot number where the car is parked.
        """
        return self.car_index.get(registration_number)

    def get_parked_cars_information(self):
        """
        :return: The `car_index` maintained by the object instance.
        """
        return self.car_index


@dataclass
class Ticket:
    car: Car
    slot: int
