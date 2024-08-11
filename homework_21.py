import unittest


def calculate_discounted_price(price, discount):
    """
    Розраховує ціну після знижки.

    :param price: Початкова ціна товару.
    :param discount: Відсоток знижки (від 0 до 100).
    :return: Ціна після знижки.
    """
    if price < 0:
        raise ValueError("Ціна не може бути менше 0.")
    if discount < 0 or discount > 100:
        raise ValueError("Відсоток знижки повинен бути між 0 і 100.")

    discounted_price = price - (price * (discount / 100))
    return discounted_price


class TestCalculateDiscountedPrice(unittest.TestCase):

    def test_valid_discount(self):
        self.assertEqual(calculate_discounted_price(100, 20), 80.0)
        self.assertEqual(calculate_discounted_price(50, 50), 25.0)
        self.assertEqual(calculate_discounted_price(200, 0), 200.0)
        self.assertEqual(calculate_discounted_price(100, 100), 0.0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_discounted_price(-50, 20)

    def test_discount_greater_than_100(self):
        with self.assertRaises(ValueError):
            calculate_discounted_price(100, 110)

    def test_discount_less_than_0(self):
        with self.assertRaises(ValueError):
            calculate_discounted_price(100, -10)


if __name__ == '__main__':
    unittest.main()
