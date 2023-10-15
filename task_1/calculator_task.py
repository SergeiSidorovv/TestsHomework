'''
В классе Calculator создайте метод calculateDiscount,
который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
Не забудьте написать тесты для проверки этого поведения.
'''


class Calculator:
    def calculate_discount(self, price_buy: int and float, percentage_sale: int) -> float:
        if isinstance(price_buy, (int, float)) and isinstance(percentage_sale, int):
            sale = price_buy * percentage_sale / 100
            finally_sum = price_buy - sale
            return finally_sum

        else:
            raise ArithmeticError('Недопустимые аргументы')
