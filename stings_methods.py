
ticket_price = 500


taxi_to_park = 600
taxi_from_park = taxi_to_park * 1.2


pizza_price = 250
discount_percentage = 15
discount_amount = pizza_price * (discount_percentage / 100)
final_pizza_price = pizza_price - discount_amount


air_hockey_price = 8 * 80


total_cost = (ticket_price + taxi_to_park + taxi_from_park + (2 * final_pizza_price) + air_hockey_price) / 4


print("Кожен з вас повинен заплатити:", total_cost, "гривень")
