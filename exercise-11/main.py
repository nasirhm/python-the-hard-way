print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)

# Raw input is used to take raw input from a key input device like keyboard.
# Replaced as input() in Python3

# Taking input and converting it to int
print "Type a number to convert into int"
x = int(raw_input())
print x