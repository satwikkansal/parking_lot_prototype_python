from enum import Enum


class Command(Enum):
    """
    Enumerates the commands understood by the service.
    """
    CREATE_LOT = 'create_parking_lot'
    PARK = 'park'
    LEAVE = 'leave'
    STATUS = 'status'
    SLOTS_BY_COLOR = 'slot_numbers_for_cars_with_colour'
    CARS_BY_COLOR = 'registration_numbers_for_cars_with_colour'
    SLOT_FOR_CAR_NUMBER = 'slot_number_for_registration_number'
    EXIT = 'exit'
