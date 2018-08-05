# Exercise 4: Variable And Names
# Programmers use the variable names to make their code read more like English,
#  and because they have lousy memories. If they didn't use good names for things
#  in their software, they'd get lost when they tried to read their code again.


cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."

# print each names and variables

print cars, space_in_a_car, drivers, cars_not_driven, cars_driven, carpool_capacity, average_passengers_per_car

# NOTE : The '_' in **space_in_a_car** is called an **underscore character**. Find
#  out how to type it if you do not already know. We use this character a lot to
#  put an imaginary space between words in variables names
