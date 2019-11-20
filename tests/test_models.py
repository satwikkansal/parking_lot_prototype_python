import unittest

from src.models import ParkingLot, Car


class TestModels(unittest.TestCase):

    def setUp(self) -> None:
        self.parking_lot = ParkingLot(2)
        self.test_car = Car("test-car-number", "Black")

    def test_parking_lot_is_full(self):
        parking_lot = ParkingLot(1)
        # When slots are available
        self.assertFalse(parking_lot.is_full())

        # When slots are not available
        parking_lot.park(self.test_car)
        self.assertTrue(parking_lot.is_full())

    def test_park(self):
        parking_lot = self.parking_lot
        ticket = parking_lot.park(self.test_car)
        self.assertEqual(self.test_car, parking_lot.slots[0])
        self.assertIn(self.test_car.registration_number, parking_lot.car_index)
        self.assertIn(
            ticket,
            parking_lot.color_index[self.test_car.color])

        # Car number 2
        another_car = Car("another-car-number", "Blue")
        ticket = parking_lot.park(another_car)
        self.assertEqual(another_car, parking_lot.slots[1])
        self.assertIn(another_car.registration_number, parking_lot.car_index)
        self.assertIn(
            ticket,
            parking_lot.color_index[another_car.color])

        # Testing when full
        yet_another_car = Car("yet-another-car-number", "Blue")
        ticket = parking_lot.park(yet_another_car)
        self.assertIsNone(ticket)

    def test_evict(self):
        parking_lot = self.parking_lot
        ticket = parking_lot.park(self.test_car)

        # Car number 2
        another_car = Car("another-car-number", "Blue")
        ticket = parking_lot.park(another_car)

        evicted_car = parking_lot.evict(0)
        self.assertEqual(evicted_car, self.test_car)

        # Evict from already empty slot
        evicted_car = parking_lot.evict(0)
        self.assertIsNone(evicted_car)

        # Testing if slot can be filled again
        yet_another_car = Car("yet-another-car-number", "Blue")
        ticket = parking_lot.park(yet_another_car)
        self.assertEqual(yet_another_car, parking_lot.slots[0])
        self.assertIn(yet_another_car.registration_number, parking_lot.car_index)
        self.assertIn(
            ticket,
            parking_lot.color_index[yet_another_car.color])

    def test_get_cars_by_color(self):
        # Black car
        parking_lot = ParkingLot(3)
        ticket = parking_lot.park(self.test_car)

        # Blue car
        another_car = Car("another-car-number", "Blue")
        ticket = parking_lot.park(another_car)

        # Another blue car
        yet_another_car = Car("yet-another-car-number", "Blue")
        ticket = parking_lot.park(yet_another_car)

        self.assertEqual([self.test_car], parking_lot.get_cars_by_color(self.test_car.color))
        self.assertCountEqual([another_car, yet_another_car], parking_lot.get_cars_by_color(another_car.color))
        self.assertEqual([], parking_lot.get_cars_by_color("Some random color"))

    def test_get_slots_by_color(self):
        parking_lot = ParkingLot(3)
        ticket = parking_lot.park(self.test_car)

        another_car = Car("another-car-number", "Blue")
        ticket = parking_lot.park(another_car)

        yet_another_car = Car("yet-another-car-number", "Blue")
        ticket = parking_lot.park(yet_another_car)

        self.assertEqual([0], parking_lot.get_slots_by_color(self.test_car.color))
        self.assertCountEqual([1, 2], parking_lot.get_slots_by_color(another_car.color))
        self.assertEqual([], parking_lot.get_slots_by_color("Some random color"))

    def test_get_slot_number_for_car(self):
        parking_lot = self.parking_lot
        ticket = parking_lot.park(self.test_car)

        another_car = Car("another-car-number", "Blue")
        ticket = parking_lot.park(another_car)

        self.assertEqual(0, parking_lot.get_slot_number_for_car(self.test_car.registration_number))
        parking_lot.evict(0)
        self.assertIsNone(parking_lot.get_slot_number_for_car(self.test_car.registration_number))
