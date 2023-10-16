from unittest import TestCase, main
from car import Car
from vehicle import Vehicle
from motorcycle import Motorcycle


class VehicleTest(TestCase):
    def test_parent_class_car(self):
        car = Car('Audi', 'a3', 2015)
        self.assertIsInstance(car, Vehicle)

    def test_car_count_num_wheels(self):
        car = Car('Mersedes', '200', 2002)
        self.assertEqual(car.get_num_wheels(), 4)

    def test_motorcycle_count_num_wheels(self):
        motorcycle = Motorcycle('Yamaha', '345', 2020)
        self.assertEqual(motorcycle.get_num_wheels(), 2)

    def test_car_speed_test_drive(self):
        car = Car('BMW', '300', 0)
        self.assertEqual(car.test_drive(), 60)

    def test_motorcycle_speed_test_drive(self):
        mortorcycle = Motorcycle('mazeratti', '[[[', 1000000)
        self.assertEqual(mortorcycle.test_drive(), 75)

    def test_car_speed(self):
        car = Car('Volga', '1', 1999)
        self.assertEqual(car.test_drive(), 60)
        self.assertEqual(car.park(), 0)

    def test_motorcycle_speed(self):
        motorcycle = Motorcycle('..', ',,', 100)
        self.assertEqual(motorcycle.test_drive(), 75)
        self.assertEqual(motorcycle.park(), 0)


if __name__ == '__main__':
    main()
