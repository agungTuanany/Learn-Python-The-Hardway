# Exercise 11: Asking Questions
#
# Now it is time to pick up the pace. I have got you doing a lot of printing so
#  that you get used to typing simple things, but those simple things are fairly
#  boring. What we want to do now is get data into your programs. This is a little
#  tricky because you have ti learn to do two things that may not make sense
#  right away.
#
# Most of what software does is the following:
#
#       1. Take some kind input from a person
#       2. Change it.
#       3. Print out something to show how it changed.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
        age, height, weight
        )

# NOTE: Notice that we put a ** , ** (comma) at the end of each print line. This
#  is so that print doesn't end the line with a new line character and go to the
#  next line.

# How do I get a number from someone so I can do math?
#
# That's a little advanced, nit try ** x = int(raw_input()), which gets the number
#  as a string from **raw_input()** then converts it to an integer using **int()**.

# What's the difference between **input()** and **raw_input()**?
#
# The **input()** function will try convert things you enter as if they were
#  Python code, but it has security problems so you should avoid it.
