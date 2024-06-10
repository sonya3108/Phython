
ticket_price = 500
num_people = 4
taxi_to = 600
taxi_back = taxi_to * 1.2
pizza_price = 250
num_pizzas = 2
pizza_discount = 0.15
air_hockey_price = 80
num_games = 8


total_tickets = ticket_price * num_people
total_taxi = taxi_to + taxi_back
total_pizza = (pizza_price * num_pizzas) * (1 - pizza_discount)
total_air_hockey = air_hockey_price * num_games

total_cost = total_tickets + total_taxi + total_pizza + total_air_hockey
cost_per_person = total_cost / num_people

print(cost_per_person)


