# Parameters, Unpacking, Variables by using sys module
from sys import argv

script, first, second, third = argv

# script = file name

print "The script is called:", script
print "The first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# For execution python2 main.py <first> <second> <third>
