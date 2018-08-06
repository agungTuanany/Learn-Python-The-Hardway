# Exercise 16: Reading and Writing Files
#
# For now, these are the important commands you need to know. Some of them take
#  parameters, but we do not rally care about that. You only need to remember
#  that write a parameter of a string you want to write to the file.

# Let's use some of this to make a simple little text editor:

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL_C (^C)."
print "If you do wan that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print "And finally, we close it."
target.close()
