# Sting Formats in Python
my_name = "Zed A. Shaw"
my_age = 35
my_height = 74
my_weight = 180
my_eyes = "Blue"
my_teeth = "white"
my_hair = "brown"

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy" % my_weight
print "Actually that's not much of a heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usally %s depending on the coffee." % my_teeth

# A tricky line
print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)