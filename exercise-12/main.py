# Prompting in raw_input()

name = raw_input("Name? ")
age = raw_input("How ld are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So you're %r old, %r tall & %r heavy." % (age, height, weight)

# In terminal run `pydoc2 raw_input`