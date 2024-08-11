import pytest



def calculate_discounted_price(price, discount):
    """
    Розраховує ціну після знижки.

    :param price: Початкова ціна товару.
    :param discount: Відсоток знижки (від 0 до 100).
    :return: Ціна після знижки.
    """
    if price < 0:
        raise ValueError("Ціна не може бути меншою за 0.")
    if discount < 0 or discount > 100:
        raise ValueError("Знижка повинна бути в межах від 0 до 100 відсотків.")

    return price - (price * discount / 100)



def test_calculate_discounted_price():
    price = 100
    discount = 20
    expected_result = 80.0
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected_result


def test_calculate_discounted_price_zero_discount():
    price = 100
    discount = 0
    expected_result = 100.0
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected_result


def test_calculate_discounted_price_full_discount():
    price = 100
    discount = 100
    expected_result = 0.0
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected_result


def test_calculate_discounted_price_negative_price():
    with pytest.raises(ValueError):
        calculate_discounted_price(-100, 20)


def test_calculate_discounted_price_excess_discount():
    with pytest.raises(ValueError):
        calculate_discounted_price(100, 120)


def test_calculate_discounted_price_negative_discount():
    with pytest.raises(ValueError):
        calculate_discounted_price(100, -20)


@pytest.mark.parametrize("price, discount, expected_result", [
    (200, 10, 180.0),
    (50, 50, 25.0),
    (150, 30, 105.0)
])
def test_calculate_discounted_price_parametrized(price, discount, expected_result):
    actual_result = calculate_discounted_price(price, discount)
    assert actual_result == expected_result



if __name__ == "__main__":
    pytest.main()
