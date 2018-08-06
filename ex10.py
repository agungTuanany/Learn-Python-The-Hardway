# Exercise 10: What Was That?
#
# In Exercise 9 I threw you some new stuff, just to keep you on your toes. I
#  showed you two ways to make a string that goes across multiple lines. In the
#  first way, I put the characters **\n** (backslash n) between the names of the
#  month. What these two characters do is put a new line character into the
#  string at that point.
#
# This use of the **\** (backslash) character is a way we can put difficult-to-type
#  characters into a string. There are plenty of these "escape sequences" available
#  fir different characters you might want to put int, but there's special one,
#  the double backslash, which is just two of them **\**. These two characters
#  will print just one backslash. We'll try a few of theses sequences so you can
#  see what I mean.
#
# Another important escape sequence is to escape a single-quote ** ' ** or
#  double-quote ** " **. Imagine you have a string that uses double-quotes and
#  you want to put a double-quotes in for the output. If you do this "I "understand"
#  joe." then Python will get confused since it will think the ** " ** around
#  "understand" actually *ends* the string. You need a way yo tell Python that
#  the ** " ** inside the string isn't real double-quote.
#
# To solve this problem, you escape double-quotes and single-quotes so Python
#  knows what to include in the string. Here's an example
#
#       "I am 6'2\" tall." # escape double-quote inside string
#       'I am 6\'2" tall,' # escape single-quote inside string
#
# The second way is by using triple-quotes, which is just ** """ ** and works
#  like string, but you also can put as many lines of text you want until you
#  type ** """ ** again. We'll also play with these.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


fat_cat = """
I'll do list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Here's a tiny piece of fun code to try out.
while True:
    for i in ["/", "-","|","\\","|"]:
        print "%s\r" % i,

# What makes **\\** special compared to the other ones?
#
# It's simply the way you would write out one backslash (\) characters. Think
#  about why you would need this.

# When I write **//** or **/n** it doesn't work.
#
# That because you are using a forward-slash **/** and not a backslash **\**.
#  They are different characters that do very different things.

# What's better, ** ''' ** or ** """ **?
#
# It's entirely based on style. Go with the ** ''' ** (triple-single-quotes)
#  style for now, but ready to use either, depending on what feels best or what
#  everyone else is doing.
