# Exercise 12: Prompting People.

# When you typed **raw_input()**, you were typing the ( and ) characters, which
#  are parenthesis characters. This is similar to when you used them to do a
#  format with extra variables, as in **"%s %s" % (x, y).** For **raw_input**,
#  you want for the prompt inside the () so that is looks like this:
#
#       y = raw_input("Name? ")
#
# This prompts the user with "Name?" and puts the result into the variable **y**.
#  This is how you ask someone a question and get the answer.
#
# This means we can completely rewrite our previous exercise using just **raw_input**
#  to do all the prompting.

age = raw_input("how old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

#print "So, you're %r old, %r tall and %r heavy." % (
#        age, height, weight
#        )

# Type **pydoc raw_input**. To see raw_input documentation.

# using **%s** instead **%r**
print "So, you're %s old, %s tall and %s heavy." % (
        age, height, weight
        )
