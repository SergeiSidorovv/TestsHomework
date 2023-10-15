from calculator_task import Calculator
from unittest import TestCase, main


class CalculatorTest(TestCase):
    def test_first_argument_str(self):
        with self.assertRaises(ArithmeticError) as err:
            Calculator.calculate_discount(self, '', 30)

        exeption_argument = err.exception
        self.assertEqual(exeption_argument.args[0], 'Недопустимые аргументы')

    def test_first_argument_list(self):
        with self.assertRaises(ArithmeticError) as err:
            Calculator.calculate_discount(self, [12, 31], 16)

        exeption_argument = err.exception
        self.assertEqual(exeption_argument.args[0], 'Недопустимые аргументы')

    def test_second_argument_typle(self):
        with self.assertRaises(ArithmeticError) as err:
            Calculator.calculate_discount(self, 62.22, ('', 123, 55))

        exeption_argument = err.exception
        self.assertEqual(exeption_argument.args[0], 'Недопустимые аргументы')

    def test_second_argument_str(self):
        with self.assertRaises(ArithmeticError) as err:
            Calculator.calculate_discount(self, 10, 'asd')

        exeption_argument = err.exception
        self.assertEqual(exeption_argument.args[0], 'Недопустимые аргументы')

    def test_type_finally_price(self):
        self.assertIsInstance(
            Calculator.calculate_discount(self, 100, 10), float)

    def test_finally_price(self):
        self.assertEqual(Calculator.calculate_discount(self, 50.5, 10), 45.45)

    def test_first_argument_is_zero(self):
        self.assertEqual(Calculator.calculate_discount(self, 0, 25), 0.0)

    def test_first_argument_is_million(self):
        self.assertEqual(Calculator.calculate_discount(
            self, 1_000_000, 8), 920_000.0)

    def test_second_argument_is_zero(self):
        self.assertEqual(Calculator.calculate_discount(
            self, 50_000, 0), 50_000.0)

    def test_second_argument_is_hundred(self):
        self.assertEqual(Calculator.calculate_discount(
            self, 39_331.57, 100), 0.0)


if __name__ == '__main__':
    main()
