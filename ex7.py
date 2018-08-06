# Exercise 7: More Printing

# Now we are going to do a bunch of exercise where you just type code in and make
#  it run. I won't be explaining this exercise because it is more of the same.
#  The purpose is to build up your chops.

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # What'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. Try removing it to see what happen
# if you remove ** , ** that will be make a new print line

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

print "." * 10 # What'd that do?
print end7 + end8 + end9 + end10 + end11 + end12
print end1 + end2 + end3 + end4 + end5 + end6

# Why are you using the variable named 'snow'?
#
# That's actually not a variable: it is just a string with the world **snow** in
#  it. A variable wouldn't have the single-quotes around it.

# Couldn't you just not use the comma ** , ** and turn the last two lines into 
#  one single-line print?
#
# Yes, you could very easily, but then it'd be longer then 80 characters, which
#  in Python is bad style.
