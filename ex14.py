# Exercise 14: Prompting and Passing
#
# Lest done one exercise that uses **argv** and **raw_input** together to ask the
#  user something specific. You will need this for the next exercise, where we
#  learn to read and write files. In this exercise, we'll use **raw_input**
#  slightly differently by having it just print simple > prompt. This is similar
#  to a game like Zork or Adventure.

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
and you have a %r computer. Nice
""" % (likes, lives, computer)

# I don't understand what you mean by changing the prompt?
#
# See the variable **prompt = '>'**. Change that to have a different value. You
#  know this; it's just a string and you've done 13 exercise making them, so take
#  the time to figure it out.
