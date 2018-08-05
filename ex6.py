# Exercise 6: String and text

# Wile you have been writing strings, you still do not know how about they do.
#  In this exercise we create a bunch of variable with complex strings so you can
#  see what they are for. First an explanation of strings.

# A String is usually a bit of text you want to display to someone, or "export"
#  out of the program you are writing. Python knows you want something to be a
#  string when you put either ** " ** (double-quotes) around the text. You saw
#  this many times with your use of **print** when you put the text you want to
#  go inside the string inside ** " ** or ** ' ** after **print** to print the
#  string.

# String may contain the format characters you have discovered so far. You can
#  simply put the formatted variables in the string, and then a ** % ** (percent)
#  character, followed by the variable. The *only* catch is that if you want
#  multiple formats in your string to print multiple variables, you need to put
#  them inside **()** (parenthesis) separated by ** , ** (commas). It's as if you
#  were telling me to buy a list of items from the store and you said, "I want 
#  milk, eggs, bread, and soup". Only as a programmer we say, "(milk, eggs, bread,
#  soup)."

# We will now type in a whole bunch of strings, variables, and formats, and print
#  them. You will also practice using short abbreviated variables names.
#  Programmers love saving time at your expenses by using annoyingly short and
#  cryptic variables names, so let's get you started reading and writing them
#  early on.

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

print w + e #adding string with **2** variables

# What is the different between **%r** and **%s**?
#
# Use the **%r** for debugging, since it display the "raw" data of the variable,
#  but the others are used for displaying to users.

#What's the point **%s** and **%d** when you can just use **%r** ?
#
#The **%r** is best for debugging, and the other formats are actually displaying
# variables to users.
