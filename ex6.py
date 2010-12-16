# the variable x is this string, where %d is replaced by 10
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# y is a string, where it is those who know binary and those who don't
y = "Those who know %s and those who %s." % (binary, do_not)

# print both of the strings
print x
print y

# print that i said the strings, using single quote marks around them by using %r or '%s'
print "I said: %r." % x
print "I also said: '%s'." % y

# hilarious is set at the boolean false
hilarious = False
# this is a variable that is a string with a format character inside it
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the string above, replacing %r with hilarous, which is set at false
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# prints both of the above strings with no breaks or spaces
print w + e
