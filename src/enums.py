from enum import Enum


class Command(Enum):
    """
    Enumerates the commands understood by the service.
    """
    CREATE_LOT = 'create_parking_lot'
    PARK = 'park'
    LEAVE = 'leave'
    STATUS = 'status'
    SLOTS_BY_COLOUR = 'slot_numbers_for_cars_with_colour'
    CARS_BY_COLOUR = 'registration_numbers_for_cars_with_colour'
    SLOT_FOR_CA_NUMBER = 'slot_number_for_registration_number'
    EXIT = 'exit'
