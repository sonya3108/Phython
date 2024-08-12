def calculate_discounted_price(price, discount):
    """
    Calculates the price after applying a discount.

    :param price: Initial price of the item.
    :param discount: Discount percentage (from 0 to 100).
    :return: Price after discount.
    """
    if price < 0:
        raise ValueError("Price cannot be less than 0.")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100 percent.")

    return price - (price * discount / 100)