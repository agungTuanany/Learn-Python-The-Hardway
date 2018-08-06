# Exercise 20: Functions and Files
#
# Remember your checklist for functions, then do this exercise paying close
#  attention to how functions and files can work together to make useful stuff.


from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's print the whole file: \n"

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# Pay close attention to how we pass in the current line number each time we run
#  **print_a_line**.

