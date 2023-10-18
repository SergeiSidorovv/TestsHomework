from numer_interval import NumberInterval
from unittest import TestCase, main


class TestNumberInterval(TestCase):
    def test_number_interval(self):
        number = NumberInterval()
        self.assertEqual(number.number_interval(55), True)


if __name__ == '__main__':
    main()
