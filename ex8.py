# Exercise 8: Printing, Printing

# We will now see how to do a more complicated formatting of a string. This code
#  looks complex, but if you do your comments above each line and break each thing
#  down to its parts, you'll understand it.

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print "*" * 10
print "this use a double quotes"
print formatter % ("one", "two", "three", "four")
print "*" * 10
print "this use a single quotes"
print formatter % ('one', 'two', 'three', 'four')
print "*" * 10
print formatter % (True, False, False, True)
print "*" * 10
print formatter % (formatter, formatter, formatter, formatter)
print "*" * 10
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
        )
# Study this carefully and try to see how I put the **formatter** inside the
#  **formatter**


# Should I use **%s** or **%r** for formatting?
#
# You should use **%s** and only use **%r** for getting debugging information
#  about something. The **%r** will give you the "raw programmer's" version of
#  variable, also known as the "representation."

# Why do I have to put quotes around but not around **True** or **False**?
#
# Python recognizes **True** and **False** as keyword representing the concept
#  of true and false. If you put quotes around them then they are turned into
#  strings and won't work.
