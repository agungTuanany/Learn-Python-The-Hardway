# Exercise 15: Reading Files.
# This exercise involves writing two files. One is your usual ex15.py file that
#  you will run, but the other is named ex15_sample.txt. This second file isn't
#  a script but a plain text file we'll be reading in our script. Here are the
#  contents of that file:
#
#       This is stuff I typed into a file.
#       it is really cool stuff.
#       lots and lots of fun to have in here.
#
# What we want to do is "open" that file in our script and print it out. However,
#  we do not want to just "hard code" the name **ex15_sample.txt into our script.
#  "Hard coding" means putting some bit of information that should come from the
#  user as a string right in our program. That's bad because we want it to load
#  other files later. The solution is to use **arv** and **raw_input** to ask the
#  user what file the user want instead of "hard coding" the file's name.

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
