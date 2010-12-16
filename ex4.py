cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# the number of cars not driven will equal the total number of cars less the number of drivers that take cars
cars_not_driven = cars - drivers
# the number of cars driven will be the number of drivers
cars_driven = drivers
# the total capacity for people will be equal to the number of cars driven multiplied by the space per car
carpool_capacity = cars_driven * space_in_a_car
# the average passengers per car to transport everyone will be the number of passengers divided by the number of cars that are being driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
