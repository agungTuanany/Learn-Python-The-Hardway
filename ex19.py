# Exercise 19: Functions and Variables
#
# Functions may have been a mind-blowing amount of information, but do not worry.
#  Just keep doing these exercise and going through your checklist from the last
#  exercise and you will eventually get in.
#
# There is one tiny point thought that you might not have realized, which we'll
#  reinforce right now. The variables in your function are not connected to the
#  variables in your script. Here's an exercise to get you think about this:

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "Or, we can variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# This shows all the different ways we're able to give our function **cheese_and_crackers**
#  the value it needs to print them. We can give it straight numbers. We can give
#  it variables. We can give it math. We can even combine math and variables.
#
# In a way, the arguments to a function are kind of like our = character when we
#  make a variable. In fact, if you can use = to name something, you can usually
#  pass it to a function as an argument.

# What if I want to ask the user for the numbers of cheese and crackers?
#
# Remember, you just need to use int() to convert what you get from raw_input()
