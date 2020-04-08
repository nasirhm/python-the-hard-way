# Some more strings formatting
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

y = "Those who know %s and and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# %r displays the raw variable and should be only used for debugging
# %s for displaying it to other users