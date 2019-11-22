import sys
from enums import Command
from models import ParkingLot, Car


class ParkingLotController:
    """
    This class acts like a bridge between the main execution engine and the data models.
    """

    @staticmethod
    def execute_command(parking_lot: ParkingLot, command, args):
        output = None
        if parking_lot is None and command != Command.CREATE_LOT:
            # raise ValueError("The ParkingLot instance is not yet initialized")
            output = "Parking lot is not defined"

        if command is Command.CREATE_LOT:
            # Initialize parking lot
            size = int(args[0])
            parking_lot = ParkingLot(size)
            output = f'Created a parking lot with {size} slots'

        elif command is Command.PARK:
            registration_number, color = args[0], args[1]
            car = Car(registration_number, color)
            ticket = parking_lot.park(car)
            if ticket is None:
                output = 'Sorry, parking lot is full'
            else:
                output = f'Allocated slot number: {ticket.slot}'

        elif command is Command.LEAVE:
            slot_number = int(args[0])
            car = parking_lot.evict(slot_number - 1)
            if car:
                output = f'Slot number {slot_number} is free'
            else:
                output = 'Incorrect slot number'

        elif command is Command.CARS_BY_COLOR:
            color = args[0]
            cars = parking_lot.get_cars_by_color(color)
            output = ", ".join([car.registration_number for car in cars])

        elif command is Command.SLOTS_BY_COLOR:
            color = args[0]
            slots = parking_lot.get_slots_by_color(color)
            output = ", ".join([f'{slot}' for slot in slots])

        elif command is Command.SLOT_FOR_CAR_NUMBER:
            registration_number = args[0]
            slot_number = parking_lot.get_slot_number_for_car(registration_number)
            if slot_number is not None:
                output = f'{slot_number}'
            else:
                output = 'Not found'

        elif command is Command.STATUS:
            car_index = parking_lot.get_parked_cars_information()
            c1, c2, c3 = "Slot No.", "Registration No", "Colour"
            w1, w2, w3 = len(c1), len(c2), len(c3)
            output_lines = [f'{c1}    {c2}    {c3}']
            for registration_number, ticket in car_index.items():
                output_lines.append(f'{ticket.slot: <{w1}}    {registration_number: <{w2}}    {ticket.car.color}')
            output = '\n'.join(output_lines)

        elif command is Command.EXIT:
            # Exit gracefully
            sys.exit(0)

        return parking_lot, output
