# Python format characters

# Check this link out : https://docs.python.org/2.4/lib/typesseq-strings.html

# Refactoring previous code, I love Pycharm <3
# Sting Formats in Python
name = "Zed A. Shaw"
age = 35
height = 74
weight = 180
eyes = "Blue"
teeth = "white"
hair = "brown"

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy" % weight
print "Actually that's not much of a heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usally %s depending on the coffee." % teeth

# A tricky line
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)