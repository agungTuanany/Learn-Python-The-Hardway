# Exercise 18: Names. Variables, Code, Functions
#
# Big title, right? I am about to introduce you to the function! Dum dum dah!
#  Every programmer will go on and on about functions and all the different ideas
#  about how they work and what they do, but I will give you the simplest
#  explanation you can use right now.

# Function do three things:
#
#    1. They name pieces of code the way variables name string and numbers
#    2. They take arguments the way your scripts take argv.
#    3. Using #1 and #2 they let you make your own "mini-scripts" or "tiny-commands"
#
# You can create a function by using the word def in Python. I'm going to have
#  you make four different functions that work like your scripts, and I'll then
#  show you how each one is related.


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2:%r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r" % arg1

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one_takes no arguments
def print_none():
    print "I got nothing'."

print_two("Zed", "Shaw")
print_two_again("zed", "Shaw")
print_one("First!")
print_none()
