cars = 100
space_in_a_car = 4.0 # 浮点数
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are ", cars, "cars available.")
print("There are only ", drivers, "drivers avialable.")
print("There will be", cars_not_driven, "empty cars today.")
print("we can transport",carpool_capacity, "people today")
print("we need to put about", average_passengers_per_car, "in each cars")
