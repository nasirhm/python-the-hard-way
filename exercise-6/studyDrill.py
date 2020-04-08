# Assigning x
x = "There are %d types of people." % 10

# Assigning binary and do_not
binary = "binary"
do_not = "don't"

# assigning y with 2 string formatters
# string inside a string
y = "Those who know %s and those who %s." % (binary, do_not)

# printing x & y
print x
print y

# printing x and y with string formatter
# string inside a string x 2
print "I said: %r." % x
print "I also said: '%s'." % y

# Boolean
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Providing value to joke evaluation
# string inside a string
print joke_evaluation % hilarious

# assigning w, e variables
w = "This is the left side of..."
e = "a string with a right side."

# printing w + e
# concatenating w and e, appends the next one at the end of the first one.
print w + e